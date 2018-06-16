'use strict';

import {doAjaxGet} from "./AjaxUtility.js";

const aRatingIds = ["starA", "star0", "star1", "star2", "star3", "star4", "star5"];
const sRangeId = "rangeSliderFilter";
const sDimensionCheckboxPrefix = "filterChoice";
const sAllCheckboxPrefix = "filterAllCheckBox";
const sAllText = "ALL";
const sAllStar = aRatingIds[0];
const sResetButton = "filterResetButton";
const sApplyButton = "filterApplyButton";

export default class FilterAgent {
    constructor(oFilterMetadata) {
        this._filterMetadata = oFilterMetadata;
        this.initRatings();
        this.initPriceRanges();
        this.initDimensionModel();

        this.setupControlButtons();
    }

    initPriceRanges() {
        const oRangeMetadata = this.getRangeMetadata();
        const oRangeSlider = FilterAgent.getJqueryObject(sRangeId);
        this.oRange = $.extend(true, {}, oRangeMetadata);
        this.oRange.slider_checkbox = oRangeSlider;

        oRangeSlider.slider({
            tooltip: 'always',
            formatter: value => {
                return value;
            }
        });

        oRangeSlider.on('change', (oEvent) => {
            const oNewValue = oEvent && oEvent.value && oEvent.value.newValue;

            if (oNewValue) {
                this.updatePriceRanges(oNewValue);
            }
        });
    }

    updatePriceRanges(oUpdateTuple) {
        const oRange = this.oRange;

        if (this.oRange) {
            oRange.selected_min = oUpdateTuple[0];
            oRange.selected_max = oUpdateTuple[1];
        }
    }

    /**
     * rating metadata is optional parameter
     * if none was given to us, then we know it is a regular page load with no previous state
     */
    initRatings() {
        if (!this.getRatingMetadata()) {
            const oFilterMetadata = this.getFilterMetadata();
            oFilterMetadata.ratings = {};
            // no rating response from server, create default mapping without checking state
            const aRatings = aRatingIds.map((sRatingId) => {
                const oMappedRating = {
                    "star_num": parseInt(sRatingId.substr(sRatingId.length - 1)),
                    "star_id": sRatingId,
                    "star_checkbox": FilterAgent.getJqueryObject(sRatingId),
                    "was_checked": false
                };

                oFilterMetadata.ratings[sRatingId] = oMappedRating;
                return oMappedRating;
            });

            this.mRatings = new Map();
            aRatings.forEach((oRating) => {
                this.mRatings.set(oRating.star_id, oRating);
            });

            const oAllStarCheckbox = this.mRatings.get(sAllStar).star_checkbox;
            this.attachAllCheckboxListener(oAllStarCheckbox);
        } else {
            // make sure to recheck appropriate checkboxes to match previous state
        }
    }

    initDimensionModel() {
        const oDimensionMetadata = this.getDimensionMetadata();

        if (oDimensionMetadata) {
            this.mDimensions = new Map();
            const aDimensionKeys = Object.keys(oDimensionMetadata);

            aDimensionKeys.forEach((sKey) => {
                const aDimensionEntries = $.extend(true, [], oDimensionMetadata[sKey]);

                aDimensionEntries.forEach((oDimensionEntry, iIndex) => {
                    let sSelector = oDimensionEntry.checkbox_id;
                    const bIsAll = oDimensionEntry.filter_value === sAllText;
                    if (bIsAll) {
                        sSelector = sAllCheckboxPrefix + sSelector;
                    } else {
                        sSelector = sDimensionCheckboxPrefix + sSelector;
                    }

                    oDimensionMetadata[sKey][iIndex].checkbox_id = sSelector;
                    oDimensionEntry.checkbox_id = sSelector;
                    oDimensionEntry.value_checkbox = FilterAgent.getJqueryObject(sSelector);
                    oDimensionEntry.ui_dimension_name = sKey;

                    if (bIsAll) {
                        // now that we have the jQuery object, attach handler
                        this.attachAllCheckboxListener(oDimensionEntry.value_checkbox);
                    }

                    this.mDimensions.set(sSelector, oDimensionEntry);
                });
            });

            this.restoreCheckboxState(Array.from(this.mDimensions.keys()));
        }
    }

    /** Used to double check and restore state upon page reloads. Assumes models have been initiated prior to calling.
     *
     * @param aElementIds     array of checkboxes to check
     */
    restoreCheckboxState(aElementIds) {
        aElementIds.forEach((sElementId) => {
            const oElementEntry = this.mDimensions.get(sElementId);
            const bChecked = oElementEntry.was_checked;
            if (bChecked) {
                const oElement = oElementEntry.value_checkbox;
                oElement.prop('checked', true);
            }
        })
    }

    /** Used to set checkboxes in bulk without caring about their present state
     *  Intended to handle "ALL" checkbox click behaviour
     *
     * @param aElementIds     array of checkboxes to check
     * @param bCheckedState   state to set checkbox to
     */
    setCheckboxState(aElementIds, bCheckedState) {
        aElementIds.forEach((sElementId) => {
            const oElementEntry = this.mDimensions.get(sElementId) || this.mRatings.get(sElementId);
            const oElement = oElementEntry.value_checkbox || oElementEntry.star_checkbox;
            if (oElement) {
                oElement.prop('checked', bCheckedState);
            }
        })
    }

    /** UI handler to tick/un-tick all checkboxes, then updates FilterAgent dimension model to match state
     *
     * @param oAllCheckbox
     */
    attachAllCheckboxListener(oAllCheckbox) {
        oAllCheckbox.on('click', function (oEvent) {
            const oClassList = oEvent && oEvent.currentTarget && oEvent.currentTarget.classList;

            if (oClassList) {
                const bAllChecked = !!oEvent.currentTarget.checked;
                const aClassList = Array.from(oClassList);
                const sSelector = aClassList.find((sClassValue) => {
                    return sClassValue.startsWith(sAllCheckboxPrefix) || sClassValue === sAllStar;
                });

                // each checkbox contained in a li
                const aSiblings = FilterAgent.getJqueryObject(sSelector).parent().siblings().children();
                aSiblings.each((index, sibling) => {
                    sibling.checked = bAllChecked;
                });

            }
        }.bind(this));
    }

    setupControlButtons() {
        this.oResetButton = FilterAgent.getJqueryObject(sResetButton);
        this.oApplyButton = FilterAgent.getJqueryObject(sApplyButton);

        this.oResetButton.on('click', function () {
            this.wipeSelections();
        }.bind(this));

        this.oApplyButton.on('click', function () {
            const oQueryJson = this.prepareSelectionsForQuery();
            doAjaxGet(oQueryJson, window.location.href);
        }.bind((this)));
    }

    wipeSelections() {
        let aDimensionCheckboxes = Array.from(this.mDimensions.values());
        aDimensionCheckboxes = aDimensionCheckboxes.map((oDimensionEntry) => {
            return oDimensionEntry.checkbox_id;
        });

        let aRatingCheckboxes = Array.from(this.mRatings.values());
        aRatingCheckboxes = aRatingCheckboxes.map((oRatingEntry) => {
            return oRatingEntry.star_id;
        });

        const aAllCheckboxes = aDimensionCheckboxes.concat(aRatingCheckboxes);
        this.setCheckboxState(aAllCheckboxes, false);

        this.oRange.slider_checkbox.slider('setValue', [this.oRange.min, this.oRange.max], true, true);
    }

    prepareSelectionsForQuery() {
        let oQueryJson = $.extend(true, {}, this.getFilterMetadata());
        this.updateDimensionSelectionState(oQueryJson.dimensions);
        this.updateRatingSelectionState(oQueryJson.ratings);
        delete this.oRange["slider_checkbox"];
        oQueryJson.ranges = this.oRange;

        return oQueryJson;
    }

    updateDimensionSelectionState(oDimensionJson) {
        const mDimensions = this.mDimensions;

        Object.keys(oDimensionJson).forEach((sKey) => {
           const oDimension = oDimensionJson[sKey];

           Object.keys(oDimension).forEach((sDimensionKey) => {
               const oDimensionEntry = mDimensions.get(oDimension[sDimensionKey].checkbox_id);

               if (oDimensionEntry) {
                   oDimensionJson[sKey][sDimensionKey].was_checked = oDimensionEntry.value_checkbox[0].checked;
               }
           })
        });

    }

    updateRatingSelectionState(oRatingJson) {
        const mRatings = this.mRatings;

        Object.keys(oRatingJson).forEach((sKey) => {
            const oDimensionEntry = mRatings.get(sKey);

            if (oDimensionEntry) {
                oRatingJson[sKey].was_checked =  oDimensionEntry.star_checkbox[0].checked;
                delete oRatingJson[sKey]["star_checkbox"];
            }
        });
    }

    getFilterMetadata() {
        return this._filterMetadata;
    }

    getDimensionMetadata() {
        return this._filterMetadata && this._filterMetadata.dimensions;
    }

    getRangeMetadata() {
        return this._filterMetadata && this._filterMetadata.ranges;
    }

    getRatingMetadata() {
        return this._filterMetadata && this._filterMetadata.ratings;
    }

    static getJqueryObject(sSelectorId) {
        return $("." + sSelectorId);
    }
}


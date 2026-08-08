# Building Fact & Proxy Method

## Objective

Future building basemap work must prefer real, redistributable footprints and must never turn a visual guess into an existing-condition fact. This file defines the reproducible hierarchy for replacing the old submission's conceptual building envelopes.

## Evidence hierarchy

1. **Official / cleared building dataset** appropriate to the claim: use geometry and attributes within its license/scope; record version, CRS and date.
2. **Verified public footprint geometry** such as a dated OSM extract under ODbL, cross-checked against another public source or field observation when practical. This may support current physical footprint evidence but not ownership, approval or statutory control.
3. **Public structured attributes** such as `building:levels`, `height`, `building`, named facility/POI records: preserve raw value, source timestamp and tag provenance. A tag is not automatically high confidence.
4. **Derived proxy** only when the transformation is reproducible and calibrated. Record input IDs, formula/model, training/calibration source, error range, confidence and known failure modes.
5. **Unknown** when no defensible source/proxy exists.

## Height / floor policy

- If an authoritative/public source gives `height`, store it as sourced physical evidence with the appropriate confidence.
- If only `building:levels` exists, keep **levels** as the sourced attribute. Do **not** multiply by an arbitrary universal floor height and publish the result as fact.
- A height estimate from levels is allowed only after a local calibration sample exists. Required record: `height_estimate = calibrated_m_per_level * levels + calibrated_offset`, calibration sample definition, MAE/RMSE or equivalent error, temporal/spatial coverage and confidence. Until then `height_m = Unknown`.
- Image-based manual “looks like N floors” counting is not acceptable as Verified data. It may be a field-survey observation only if acquisition method/date/location are recorded and a second check is possible.

## Use / function policy

- POI proves a named activity/facility clue, not full-building use, capacity, tenancy or service quality.
- Mixed-use buildings require multiple-use representation or an explicit uncertainty field.
- Marketing material can identify a candidate institution/tenant but cannot alone establish legal parcel/building use.

## Retain / renovate / demolish

No `retain / renovate / demolish / new_build` classification may be assigned as an existing-condition fact without building condition, heritage/control, ownership/implementation and professional survey evidence. Until those inputs exist, downstream geometry must be labelled **Proposed program envelope** or **Unknown existing condition**.

## Minimum derived record

`feature_id, source_id, retrieved_at, original_crs, exchange_crs, transformation_script, raw_attributes, derived_fields, formula_or_model, calibration_reference, confidence, limitations, conflict_ids`.

## Integration trigger

When official/verified current building data becomes available: replace the conceptual submission building layer only through Final Integration; rerun footprint totals, floor-area calculations, FAR status, diagrams and any retain/renovate/demolish narrative. Never let old conceptual geometry survive invisibly as Existing.

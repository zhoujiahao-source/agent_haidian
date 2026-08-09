# Field audit protocol

## Purpose

Close the evidence gaps that cannot be resolved responsibly from public documents alone: crossings, entrances, accessibility, ground-floor uses, construction closures, public-space use, actual park continuity and current service interfaces.

This protocol does **not** collect personal data, faces, device identifiers, private-property information or sensitive infrastructure details. Observation is of public space and publicly visible facilities only.

## Priority sequence

1. **Critical**: 大钟寺站四象限; 京张遗址公园全线代表样段 continuity.
2. **High**: 学知园站/学北园; 清河—小月河 interface; AI原点公共服务; 知春路缝合; 大钟寺南小街; 小月河上/中/下游样段; 中关村专业服务接口.
3. **Medium**: 清华园铁路记忆节点; 转河南缘等补充样点.

Detailed targets: `data/field_audit_targets.csv`.

## Standard capture for each target

Record:
- `target_id`;
- audit date/time and weather;
- observer name or agent/human team identifier if consented;
- GPS point/track from the observer's own device, rounded appropriately for public-space mapping;
- four-direction context photographs where legal and appropriate;
- entrance/opening status;
- pedestrian route continuity;
- cycle route / parking condition;
- accessible route, curb ramps, tactile paving, elevators where visible;
- construction fencing / closure / detour;
- ground-floor public interface categories, without identifying individual occupants beyond public signage;
- public-space activity categories and approximate counts in broad bins, not face/person tracking;
- lighting, seating, shade, toilets, drinking water, wayfinding and emergency access where visible;
- rail/water/heritage safety constraints;
- observed mismatch with OSM/Microsoft/official public pages.

## Evidence classes after field audit

A field observation can support `Verified / Known` for the **observed condition at that time and place**, but it does not create Official planning status. Statutory boundary, ownership, FAR, heritage control and engineering capacity remain Official/Unknown according to their own sources.

## Privacy and ethics

- Do not photograph or catalogue identifiable individuals as the subject of the survey.
- Do not infer demographic, disability, ethnicity, occupation or other sensitive characteristics from appearance.
- Do not enter non-public areas or bypass access controls.
- Do not document security-sensitive infrastructure beyond what is necessary for ordinary urban-design observations.
- If a facility prohibits photography, record text notes only.
- Aggregate activity observations into coarse categories/time windows.

## Repeatability

For critical samples, repeat at least three windows when feasible:
- weekday AM peak;
- weekday evening peak;
- weekend afternoon/evening.

For construction zones, repeat after major phase changes rather than assuming a planned completion date equals as-built status.

## Data schema recommendation

Each field record should contain:

```text
observation_id,target_id,observed_at,geometry_wgs84,observer_method,
access_status,pedestrian_continuity,cycle_continuity,accessibility_status,
construction_status,public_interface_categories,activity_bin,photo_refs,
source_id,evidence_class,confidence,limitations,conflict_ids
```

Use a source ID such as `FIELD-2026-<date>-<target_id>` and link the record back to the public-source IDs in `field_audit_targets.csv`.

## Completion gate

Field-audit work is complete only when:
- all critical targets have at least one observation;
- every high target is either observed or explicitly marked inaccessible/not-yet-observed;
- photo/track references are internally consistent;
- no personal-sensitive dataset was created;
- conflicts with downloaded basemap layers are recorded rather than silently overwritten;
- `spatial_evidence_register.csv` is updated only after review.

## Current status

`pending_field`. This conversation has no physical-site sensing capability. The remaining field task is therefore converted into a concrete, bounded, privacy-safe audit package rather than being falsely marked complete.

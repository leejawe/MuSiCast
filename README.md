# MuSiCast

MuSiCast is a multiscale AI–numerical fusion framework for building-scale urban wind prediction. This repository accompanies the manuscript **MuSiCast: An accurate and efficient multiscale AI–numerical fusion framework for building-scale 3D urban wind prediction from global weather forecasts**.

## Current release

This initial submission-stage release provides a real **MeteoPair-SCC v1** GraphCast–WRF paired-data demonstration. It contains one retained 64 × 64 patch at nominal 3 km reference spacing, valid at **2020-01-15 12:00 UTC**, together with latitude, longitude, terrain elevation and a land mask. The forecast and reference fields were independently generated and then aligned for supervised regional downscaling. The forecast arrays here are the already aligned inputs on the reference grid; interpolation does not create new native forecast information.

This winter regional sample is distinct from the October 2022 Changsha urban application. It is one development/illustration sample, not the complete dataset, a training split or an independent benchmark. No predictions, trained weights, or complete training pipeline are included.

## Files

- `data/meteopair_scc_v1_demo.npz` — eight physical-unit arrays, each shaped `(64, 64)`.
- `data/metadata.json` — valid time, units, grid layout and file checksum.
- `examples/read_demo.py` — loads the example and verifies its fields.
- `DATA_SOURCES.md` — access routes for public data used in the study.

The arrays are `forecast_u10`, `forecast_v10`, `reference_u10`, `reference_v10`, `latitude`, `longitude`, `elevation`, and `land_mask`. Winds are stored in m/s in the original paired-tensor component convention; no new component rotation is performed for this demo. The geographical coordinates identify cell centres. Terrain is in metres, and the land mask uses 1 for land and 0 for water.

## Read the demo

```bash
python -m pip install -r requirements.txt
python examples/read_demo.py
```

## Code availability and roadmap

**The R3diff source code will be made open source in a subsequent update to this repository.** The initial release deliberately contains the paired-data demo and a reading example only. It does not claim to provide the R3diff training or inference implementation yet. Additional documentation and data examples will be added with the code release.

## Data provenance and use

The sample is copied from the retained paired fields used in the regional reconstruction study. It has not been regenerated, reselected, normalized anew, or altered for this release. The complete source data and upstream terms are listed in `DATA_SOURCES.md`. This repository does not replace the original providers' distribution or license terms, and the public sample should not be presented as the full MeteoPair-SCC v1 dataset.

Repository: https://github.com/leejawe/MuSiCast

# Public data access

These are data actually used in the study, not every dataset cited in the literature review.

1. **ERA5 hourly single-level fields**, Copernicus Climate Data Store: https://doi.org/10.24381/cds.adbb2d47 and https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels .
2. **ERA5 hourly pressure-level fields**, Copernicus Climate Data Store: https://doi.org/10.24381/cds.bd0915c6 and https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels . A CDS account and acceptance of provider terms may be required.
3. **HRRR-Mini**, NVIDIA NGC: https://catalog.ngc.nvidia.com/orgs/nvidia/modulus/resources/modulus_datasets-hrrr_mini . The published benchmark pairs coarse atmospheric inputs and high-resolution HRRR fields from 2018–2021. This repository does not redistribute it.
4. **NOAA/CIRA AI Weather Prediction Model Reforecasts**, for the October 2022 Changsha case: https://registry.opendata.aws/aiwp/ . Public files are hosted in `s3://noaa-oar-mlwp-data/`; GraphCast Operational/IFS files are under `GRAP_v100_IFS/2022/1003/` for the 2022-10-03 initialization. This is a historical AI reforecast archive, not a 2022 real-time operational product and not the ERA5-initialized winter pairing experiment.

The authors generated the GraphCast–WRF pairs constituting MeteoPair-SCC v1. Only one already aligned winter development sample is distributed here. Its WRF reference and derived static fields are in the NPZ; the original global source grids and all WRF runs are not distributed in this initial release.

The public GraphCast implementation is available at https://github.com/google-deepmind/graphcast and WRF at https://github.com/wrf-model/WRF . These are software links, not additional datasets. R3diff code will follow in this repository.

The Huanghua observations and detailed urban geometry were supplied for the application and are not asserted to be unrestricted public datasets. Requests for these inputs and additional generated outputs should be directed to the corresponding author and remain subject to any relevant third-party conditions.

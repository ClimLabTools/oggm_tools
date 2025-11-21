## Introduction `oggm_tools`
This is a collection of useful OGGM workflows beyond the very good tutorials published 
on the [OGGM website](https://tutorials.oggm.org/stable). 

Before the notebooks and scripts can be executed, an OGGM environment must be installed. 
Detailed instructions can be found [here](https://docs.oggm.org/en/stable/installing-oggm.html#). 
Installing the environment from the provided `environment.yml` usually works well.

OGGM is based on the RGI. The [GLIMS Viewer](https://www.glims.org/maps/glims) is a very usuful tool to find the RGI-ID of your glacier of interest.

**Note**: the OGGM resources get constantly updated so some of the used code snippets might look differently now.


## Examples in this repository:

- Modelling **ice thickness** of an ice cap until 2100
  - OGGM workflow to generate `.nc` files
  - Plotting routines for output analysis
- **Flowline determination** for given RGI-IDs
  - extracts glacier outlines and centerlines/flowlines as vector files
  - extracts coordinates along flowline incl. surface height and slope as `.csv` file
- more to come...




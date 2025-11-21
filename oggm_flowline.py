from oggm import cfg, utils, workflow, tasks, graphics
from oggm.core import flowline
import salem
import xarray as xr
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

cfg.initialize(logging_level='WARNING')

# Where to store the data
cfg.PATHS['working_dir'] = utils.gettempdir(dirname='OGGM-flowlines', reset=True)
cfg.PARAMS['store_model_geometry'] = True

# Which glaciers?
rgi_ids = ['RGI60-11.00897']
# We start from prepro level 3 with all data ready
base_url = 'https://cluster.klima.uni-bremen.de/~oggm/gdirs/oggm_v1.6/L3-L5_files/2023.3/centerlines/W5E5/'
gdirs = workflow.init_glacier_directories(rgi_ids, from_prepro_level=3, prepro_base_url=base_url, prepro_border=80)
gdir = gdirs[0]

output_dir = utils.mkdir('outputs')
utils.write_centerlines_to_shape(gdirs, path=f'{output_dir}/centerlines.shp')

sh = gpd.read_file(f'{output_dir}/centerlines.shp')
sh.plot()
plt.show()
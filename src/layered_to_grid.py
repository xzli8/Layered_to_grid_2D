#***********************************************************
#
# Filename : layered_to_grid.py
#
# Function : From layered model to grid model
#
# Author : XingzhongLi
#
# Date : 2018/11
#
#***********************************************************

import sys
import math
import numpy as np

import mod_io
import mod_plot
import mod_layer
import mod_grid

EPS = 1e-6

# read data from shell :
filename_grid = sys.argv[1]
filename_layer = sys.argv[2]
filename_model = sys.argv[3]

v_layer = []
depth_layer = []
amplitude_layer = []
w_layer = []
z_layer = []
z_layer_all = []
v_grid = []

# get grid message and layer message :
xmin, xmax, zmin, zmax, d_grid = mod_io.input_grid(filename_grid)
num_layer, d_layer, v_layer, depth_layer, amplitude_layer, w_layer = \
mod_io.input_layer(filename_layer)

# generate layer :
nx_layer = math.ceil((xmax - xmin) / d_layer) + 1;
for i in range(0, num_layer, 1):
    z_layer = mod_layer.generate_layer(nx_layer, xmin, d_layer, \
              depth_layer[i], amplitude_layer[i], w_layer[i])
    z_layer_all += z_layer

# generate grid :
nx_grid = int((xmax - xmin + EPS) / d_grid + 1)
nz_grid = int((zmax - zmin + EPS) / d_grid + 1)
v_grid = mod_grid.generate_grid(nx_grid, nz_grid, xmin, zmin, d_grid, \
         num_layer, nx_layer, d_layer, v_layer, z_layer_all)
v_grid = np.array(v_grid)
v_grid = v_grid.reshape(nx_grid, nz_grid)
v_grid = v_grid.T

# plot model :
flag_plot_model = mod_plot.plot_model(xmin, xmax, zmin, zmax, nx_grid, \
                  nz_grid, v_grid, num_layer, nx_layer, z_layer_all)
if(flag_plot_model == 0):
    print("Plotting model succeed!")

# output data :
flag_output_model = mod_io.output_model(filename_model, xmin, xmax, \
                    zmin, zmax, d_grid, nx_grid, nz_grid, v_grid, \
                    num_layer, nx_layer, d_layer, z_layer_all)
if(flag_output_model == 0):
    print("Model generation succeed!")

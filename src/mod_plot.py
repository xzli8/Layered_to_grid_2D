#***********************************************************
#
# Filename : mod_plot.py
#
# Function : Plot 2D layered model
#
# Author : XingzhongLi
#
# Date : 2018/11
#
#***********************************************************

import numpy as np
import matplotlib.pyplot as plt

def plot_model(xmin, xmax, zmin, zmax, nx_grid, nz_grid, v_grid, \
               num_layer, nx_layer, z_layer_all):
    """Plot model"""

    # set figure size :
    x_size = 20
    z_size = x_size / (xmax - xmin) * (zmax - zmin)
    plt.figure(figsize = (x_size, z_size))
    ax = plt.gca()

    # plot velocity contour :
    x_grid = np.linspace(xmin, xmax, nx_grid)
    z_grid = np.linspace(zmin, zmax, nz_grid)
    x_grid, z_grid = np.meshgrid(x_grid, z_grid)
    plt.contourf(x_grid, z_grid, v_grid)
    cbar = plt.colorbar()
    cbar.set_label("velocity (km/s)")

    # plot layer :
    x_layer = np.linspace(xmin, xmax, nx_layer)
    for i in range(1, num_layer, 1):
        z_layer = []
        index_begin = i * nx_layer
        index_end = (i + 1) * nx_layer
        for j in range(index_begin, index_end, 1):
            z_layer.append(z_layer_all[j])
        plt.plot(x_layer, z_layer, "k-", linewidth = 1.5, label = "interface")
    
    # adjust axis :
    ax.axis("equal")
    ax.xaxis.set_ticks_position("top")
    ax.yaxis.set_ticks_position("left")
    ax.set_xlim(xmin - 1, xmax + 1)
    ax.set_ylim(zmin - 1, zmax + 1)
    ax.invert_yaxis()
    ax.xaxis.set_major_locator(plt.MultipleLocator(10.0))
    ax.yaxis.set_major_locator(plt.MultipleLocator(10.0))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1.0))
    ax.grid(which = "major", axis = "x", linewidth = 0.75, linestyle = "solid", color = "k")
    ax.grid(which = "major", axis = "y", linewidth = 0.75, linestyle = "solid", color = "k")
    ax.grid(which = "minor", axis = "x", linewidth = 0.75, linestyle = "solid", color = "k")
    ax.grid(which = "minor", axis = "y", linewidth = 0.75, linestyle = "solid", color = "k")

    # adjust figure :
    ax.set_title("Model", fontsize = 24, y = 1.05)
    ax.set_xlabel("X / m", fontsize = 14)
    ax.set_ylabel("Z / m", fontsize = 14)

    # show figure :
    plt.show() 

    return 0

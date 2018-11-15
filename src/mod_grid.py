#*********************************************************
#
# Filename : mod_grid.py
#
# Function : Generate grid for the 2D layered model
#
# Author : XingzhongLi
#
# Date : 2018/11
#
#*********************************************************

EPS = 1e-6

def linear_interpolation_1d(x1, x2, y1, y2, x0):
    """Linear interpolation in 1D case"""

    if(abs(x1 - x2) < EPS):
        y0 = (y1 + y2) / 2.0
    else:
        y0 = y1 + (y2 - y1) / (x2 - x1) * (x0 - x1)

    return y0

def layer_depth(x0, index_layer, nx_layer, xmin, d_layer, z_layer_all):
    """Calculate layer depth at x = x0, return z0"""
    
    z0 = 0.0
    index_begin = index_layer * nx_layer
    index_end = (index_layer + 1) * nx_layer
    for i in range(index_begin, index_end-1, 1):
        x1 = (i % nx_layer) * d_layer
        x2 = (i % nx_layer + 1) * d_layer
        z1 = z_layer_all[i]
        z2 = z_layer_all[i+1]
        if((x0 + EPS > x1) and (x0 - EPS < x2)):
            z0 = linear_interpolation_1d(x1, x2, z1, z2, x0)

    return z0

def generate_grid(nx_grid, nz_grid, xmin, zmin, d_grid, num_layer, \
                  nx_layer, d_layer, v_layer, z_layer_all):
    """Generate grid for the 2D model"""

    v_grid = []
    for ix in range(0, nx_grid, 1):
        x_grid = xmin + ix * d_grid

        z_layer = []
        for index_layer in range(0, num_layer, 1):
            z0 = layer_depth(x_grid, index_layer, nx_layer, xmin, 
                 d_layer, z_layer_all)
            z_layer.append(z0)

        for iz in range(0, nz_grid, 1):
            z_grid = zmin + iz * d_grid

            for index_layer in range(0, num_layer-1, 1):
                if((z_grid + EPS > z_layer[index_layer]) and \
                   (z_grid - EPS < z_layer[index_layer+1])):
                    v0 = v_layer[index_layer]
                elif(z_grid + EPS > z_layer[index_layer+1]):
                    v0 = v_layer[index_layer+1]
            v_grid.append(v0)

    return v_grid

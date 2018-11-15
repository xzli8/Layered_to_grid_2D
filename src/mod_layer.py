#************************************************************
#
# Filename : mod_layer.py
#
# Function : Generate layer for the 2D layered model
#            (use "sin" to calculate the undulating interface)
#
# Author : XingzhongLi
#
# Date : 2018/11
#
#************************************************************

import math

def generate_layer(nx_layer, xmin, d_layer, depth, amplitude, w):
    """Generate layer in the model"""

    z_layer = []
    for i in range(0, nx_layer, 1):
        x = xmin + i * d_layer
        z = math.sin(w * x) * amplitude + depth
        z_layer.append(z)

    return z_layer

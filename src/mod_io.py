#************************************************************
#
# Filename : mod_io.py
#
# Function : Provide I/O function for "layered_to_grid.py"
#
# Author : XingzhongLi
#
# Date : 2018/11
#
#************************************************************

def input_grid(filename_grid):
    """Input grid message from file"""

    f_grid = open(filename_grid, mode = "r")
    f_grid.readline()
    line = f_grid.readline().strip().split()
    xmin = float(line[0])
    xmax = float(line[1])
    zmin = float(line[2])
    zmax = float(line[3])
    f_grid.readline()
    d_grid = float(f_grid.readline())
    f_grid.close()

    return xmin, xmax, zmin, zmax, d_grid

def input_layer(filename_layer):
    """Input layer message from file"""

    f_layer = open(filename_layer, mode = "r")
    f_layer.readline()
    num_layer = int(f_layer.readline())
    f_layer.readline()
    d_layer = float(f_layer.readline())
    f_layer.readline()
    f_layer.readline()

    v_layer = []
    depth_layer = []
    amplitude_layer = []
    w_layer = []
    for i in range(0, num_layer, 1):
        line = f_layer.readline().strip().split()
        v_layer.append(float(line[0]))
        depth_layer.append(float(line[1]))
        amplitude_layer.append(float(line[2]))
        w_layer.append(float(line[3]))
    f_layer.close()

    return num_layer, d_layer, v_layer, depth_layer, \
           amplitude_layer, w_layer

def output_model(filename_model, xmin, xmax, zmin, zmax, d_grid, \
                 nx_grid, nz_grid, v_grid, num_layer, nx_layer, \
                 d_layer, z_layer_all):
    """Output model data to file"""

    f_model = open(filename_model, mode = "w")
    line = "----xmin----xmax----zmin----zmax----d----" + "\n"
    f_model.write(line)
    line = str(xmin) + "\t" + str(xmax) + "\t" + str(zmin) + \
           "\t" + str(zmax) + "\t" + str(d_grid) + "\n"
    f_model.write(line)

    line = "----P_wave Velocity----" + "\n"
    f_model.write(line)
    line = str(0) + "\t"
    for i in range(0, nx_grid, 1):
        line += str(i) + "\t"
    line += "\n"
    f_model.write(line)

    for i in range(0, nz_grid, 1):
        line = str(i) + "\t"
        for j in range(0, nx_grid, 1):
            line += str(v_grid[i, j]) + "\t"
            if(j == (nx_grid - 1)):
                line += "\n"
        f_model.write(line)

    line = "----num_itf----" + "\n"
    f_model.write(line)
    line = str(num_layer - 1) + "\n"
    f_model.write(line)
    line = "----d_rs----" + "\n"
    f_model.write(line)
    line = str(d_layer) + "\n"
    f_model.write(line)
    line = "----z_rs----" + "\n"
    f_model.write(line)
    for i in range(1, num_layer, 1):
        for j in range(0, nx_layer, 1):
            k = i * nx_layer + j
            line = str(z_layer_all[k]) + "\t"
            f_model.write(line)
        f_model.write("\n")

    f_model.close()

    return 0

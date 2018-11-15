#!/bin/bash

PY=python3
script=./src/layered_to_grid.py

input=./input
output=./output
filename_grid=$input/grid.dat
filename_layer=$input/layer.dat
filename_model=$output/model.dat

# reinitialize filename_model :
rm -rf $output
mkdir -p $output

# run EXE file :
$PY $script $filename_grid $filename_layer $filename_model

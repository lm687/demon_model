#!/bin/bash

mkdir -p output_data/BirthRateGrids
mkdir -p output_data/DriverGrids
mkdir -p output_data/PopsGrids
mkdir -p output_data/PassengersGrids
mkdir -p output_data/MigrationRateGrids

# g++ -o demon demon.cpp -I/usr/local/include/boost/ -lm #compile
# g++ -o demon demon_sig.cpp -I/usr/local/include/boost/ -lm #compile
g++ -o demon demon_sig.cpp -I/usr/local/include/boost/ -lm -std=c++14

./demon  ./ init_conf_file.dat ##output_data #execute

printf "\nEnd of execution\n"

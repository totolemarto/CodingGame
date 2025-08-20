#!/bin/bash

make clean
make FILE=$1
./main input_facile.txt > log
if diff log input_facile_sol.txt > /dev/null; then
    echo "réussite sur input facile"
else
    echo "échec sur input facile"
fi
./main  input_moyen.txt > log
if diff log input_moyen_sol.txt > /dev/null; then
    echo "réussite sur input moyen"
else
    echo "échec sur input moyen"
fi

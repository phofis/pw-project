#!/bin/bash

echo -n "" > results.txt

for i in $(seq 1 100);
do
    echo "" >> results.txt
    echo "test $i" >> results.txt
    echo "" >> results.txt
    make gen > /dev/null
    make all >> results.txt 2>&1
done

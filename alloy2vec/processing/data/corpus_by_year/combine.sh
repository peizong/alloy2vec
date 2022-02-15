#!/bin/bash

for i in {1999..2018}
do
echo $i
cat raw/$i.csv >> 2018.csv
done

#!/bin/bash

# Run benchmarks
for iteration in 1 2 3
do
    for database in redis mongo orient
    do
        ./benchmark_${database}.sh ${iteration}
    done
done

# Extract metrics
./extract_all_metrics.sh
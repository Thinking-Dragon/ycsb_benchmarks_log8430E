#!/bin/bash

mkdir orient_benchmark_$1

for workload in a b c d e f
do
    python2 ./bin/ycsb load orientdb -s -P workloads/workload${workload} > orient_benchmark_$1/load_${workload}.txt
    python2 ./bin/ycsb run  orientdb -s -P workloads/workload${workload} > orient_benchmark_$1/run_${workload}.txt
done

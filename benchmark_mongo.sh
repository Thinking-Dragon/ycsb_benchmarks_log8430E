#!/bin/bash

mkdir mongo_benchmark_$1

for workload in a b c d e f
do
    python2 ./bin/ycsb load mongodb-async -s -P workloads/workload${workload} > mongo_benchmark_$1/load_${workload}.txt
    python2 ./bin/ycsb run  mongodb-async -s -P workloads/workload${workload} > mongo_benchmark_$1/run_${workload}.txt
    sudo docker exec -it mongo-instance mongo ycsb --eval "db.dropDatabase()"
done

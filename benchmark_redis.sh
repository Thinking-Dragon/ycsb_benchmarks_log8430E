#!/bin/bash

mkdir redis_benchmark_$1

for workload in a b c d e f
do
    python2 ./bin/ycsb load redis -s -P workloads/workload${workload} -p "redis.host=127.0.0.1" -p "redis.port=6379" > redis_benchmark_$1/load_${workload}.txt
    python2 ./bin/ycsb run  redis -s -P workloads/workload${workload} -p "redis.host=127.0.0.1" -p "redis.port=6379" > redis_benchmark_$1/run_${workload}.txt
done

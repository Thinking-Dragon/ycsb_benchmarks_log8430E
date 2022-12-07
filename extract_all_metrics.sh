#!/bin/bash

echo "Database,Action,Workload,Iteration,Runtime,Throughput" > metrics.csv

for iteration in 1 2 3
do
    for database in redis mongo orient
    do
        for action in load run
        do
            for workload in a b c d e f
            do
                python3 ./extract_metrics.py $database $action $workload $iteration >> metrics.csv
            done
        done
    done
done

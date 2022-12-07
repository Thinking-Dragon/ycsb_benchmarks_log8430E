from sys import argv
import re

db_name = argv[1]
action_name = argv[2]
workload_name = argv[3]

iteration = argv[4]

file_path = db_name + '_benchmark_' + iteration + '/' + action_name + '_' + workload_name + '.txt'

with open(file_path) as file:
    runtime = ''
    throughput = ''

    for line in file:
        is_runtime    = re.search("RunTime", line)
        is_throughput = re.search("Throughput", line)

        if is_runtime:
            runtime = float(line.split(',')[2].strip())

        if is_throughput:
            throughput = float(line.split(',')[2].strip())
    
    print(db_name + ',' + action_name + ',' + workload_name + ',' + iteration + ',' + str(runtime) + ',' + str(throughput))

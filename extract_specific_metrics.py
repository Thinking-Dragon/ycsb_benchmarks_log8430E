import re

def get_metric_from_line(metrics, key, line):
    if key in metrics.keys():
        metrics[key] = metrics[key] + float(line.split(',')[2].strip())
    else:
        metrics[key] = float(line.split(',')[2].strip())

def extract_metrics(db_name, action_name, workload_name):
    metrics = dict()

    for iteration in [1, 2, 3]:
        file_path = db_name + '_benchmark_' + str(iteration) + '/' + action_name + '_' + workload_name + '.txt'

        with open(file_path) as file:

            for line in file:
                if re.search("READ.*AverageLatency", line):
                    get_metric_from_line(metrics, 'read_latency', line)
                
                if re.search("UPDATE.*AverageLatency", line):
                    get_metric_from_line(metrics, 'update_latency', line)
                
                if re.search("SCAN.*AverageLatency", line):
                    get_metric_from_line(metrics, 'scan_latency', line)
                
                if re.search("READ\-MODIFY\-WRITE.*AverageLatency", line):
                    get_metric_from_line(metrics, 'read_modify_write_latency', line)
                
                if re.search("INSERT.*AverageLatency", line):
                    get_metric_from_line(metrics, 'insert_modify_write_latency', line)
                
                if re.search("RunTime", line):
                    get_metric_from_line(metrics, 'runtime', line)

                if re.search("Throughput", line):
                    get_metric_from_line(metrics, 'throughput', line)
                
    for key in metrics.keys():
        metrics[key] = metrics[key] / 3

    return metrics

if __name__ == '__main__':
    all_metrics = dict()

    for db_name in ["redis", "mongo", "orient"]:
        for action_name in ["load", "run"]:
            for workload_name in ["a", "b", "c", "d", "e", "f"]:
                metrics = extract_metrics(db_name, action_name, workload_name)
                all_metrics[(db_name, action_name, workload_name)] = metrics

    print(all_metrics)

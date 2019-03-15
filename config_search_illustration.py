import json
import matplotlib.pyplot as plt
import numpy as np

def get_acc_list(file_dir, curve_color):
    with open(file_dir, encoding='utf-8') as f:
        # record best acc, key = time, value = acc
        best_acc = dict()
        min_start_time = np.inf
        max_end_time = 0

        data = json.load(f)

        # find the best acc of each config
        config_acc = dict()
        for trials in data:
            if trials["status"] == "SUCCEEDED":
                if "finalMetricData" not in trials.keys():
                    print ("No final metrics, trial id = ", trials["id"])
                    continue
                result_str = trials["finalMetricData"][0]["data"]
                if curve_color == "g":
                    acc = json.loads(result_str)["default"]
                else:
                    acc = float(result_str)

                params = trials["hyperParameters"]["parameters"]
                params_copy = {
                    "batch_size": params["batch_size"],
                    "conv_size": params["conv_size"],
                    "learning_rate": params["learning_rate"],
                    "hidden_size": params["hidden_size"],
                    "dropout_rate": params["dropout_rate"]
                }
                if params_copy in config_acc.keys():
                    config_acc[params_copy] = max(acc, config_acc[params_copy])
                else:
                    config_acc[params_copy] = acc

        for trials in data:
            if trials["status"] == "SUCCEEDED":
                acc = config_acc[trials["hyperParameters"]["parameter_id"]]
                # update best_acc
                if trials["endTime"] in best_acc.keys():
                    best_acc[trials["endTime"]] = max(acc, best_acc[trials["endTime"]])
                else:
                    best_acc[trials["endTime"]] = acc
                min_start_time = min(min_start_time, int(trials["startTime"]))
                max_end_time = max(max_end_time, int(trials["endTime"]))

        _length = 2100000

        x = range(0, _length + 10) 

        # generate best_acc illustration
        curr_best = 0
        y1 = [0] * int(_length + 10)
        for i in range (0, _length + 9):
            if i + min_start_time in best_acc.keys():
                curr_best = max(curr_best, best_acc[i + min_start_time])
            y1[i] = curr_best
        
        plt.scatter(x[:], y1[:], c=curve_color, marker='.')

        
plt.figure()

get_acc_list(file_dir='BOHB_MNIST_60_1_PAI_1GPU_5concu/experiment.json', curve_color="g") # green
get_acc_list(file_dir='Hyperband_MNIST_60_PAI_1GPU_5concu/experiment.json', curve_color="b") # blue
get_acc_list(file_dir='Random_MNIST_PAI_1GPU_5concu/experiment.json', curve_color="r") #red
get_acc_list(file_dir='TPE_MNIST_PAI_1GPU_5concu/experiment.json', curve_color="k") # black

plt.show()
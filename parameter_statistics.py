import json
import matplotlib.pyplot as plt
import numpy as np

""" 
{
    "lr":{"_type":"choice", "_value":[0.1, 0.01, 0.001, 0.0001]},
    "optimizer":{"_type":"choice", "_value":["SGD", "Adadelta", "Adagrad", "Adam", "Adamax"]},
    "model":{"_type":"choice", "_value":["vgg", "resnet18", "googlenet", "densenet121", "mobilenet", "dpn92", "senet18"]}
} 
"""

record_lr = [0.1, 0.01, 0.001, 0.0001, 0, 0, 0]
record_optimizer = ["SGD", "Adadelta", "Adagrad", "Adam", "Adamax", "", ""]
record_model = ["vgg", "resnet18", "googlenet", "densenet121", "mobilenet", "dpn92", "senet18"]

with open('BOHB_CIFAR10_PAI_4GPU_2concu/experiment.json', encoding='utf-8') as f:
    config_num = 0
    _success = np.zeros((5, 5))
    _filed = np.zeros((5, 5))

    data = json.load(f)
    for trials in data:
        params_id = trials["hyperParameters"]["parameter_id"]
        s = int(params_id[0])
        r = int(params_id[2])
        if trials["status"] == "SUCCEEDED":
            _success[s][r] += 1
        else:
            _filed[s][r] += 1

    for s in range(4, 1, -1):
        for r in range(0, s+1):
            print ("s = ", s, "r = ", r, "success = ", _success[s][r], " failed = ", _filed[s][r])



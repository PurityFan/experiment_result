import json

import matplotlib.pyplot as plt
import numpy as np

plt.figure()

with open('BOHB/experiment.json', encoding='utf-8') as f:
    # record best acc, key = time, value = acc
    data = json.load(f)
    for trials in data:
        y1 = []
        curve_colar = 'g'
        if trials["status"] == "SUCCEEDED":
            intermediate_result = trials["intermediate"]
            for epoch_result in intermediate_result:
                s = epoch_result["parameterId"][0]
                if s == '3':
                    r = epoch_result["parameterId"][2]
                    if epoch_result["type"] == "PERIODICAL":
                        acc = json.loads(epoch_result["data"])["default"]
                        y1.append(acc)
                    if r == '0':
                        curve_colar = 'k'
                    elif r == '1':
                        curve_colar = 'r'
                    elif r == '2':
                        curve_colar = 'y'
                    elif r == '3':
                        curve_colar = 'c'
                    elif r == '4':
                        curve_colar = 'b'
            num_point = len(y1)
            x = range(num_point)
            plt.plot(x, y1, curve_colar, linewidth=1)

plt.show()

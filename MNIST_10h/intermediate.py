import json

import matplotlib.pyplot as plt
import numpy as np

plt.figure()

def plt_curve(file_dir, curve_color):
    with open(file_dir, encoding='utf-8') as f:
        # record best acc, key = time, value = acc
        data = json.load(f)
        for trials in data:
            y1 = []
            if trials["status"] == "SUCCEEDED":
                intermediate_result = trials["intermediate"]
                for epoch_result in intermediate_result:
                    if epoch_result["type"] == "PERIODICAL":
                        if curve_color == 'g':
                            acc = json.loads(epoch_result["data"])["default"]
                        else:
                            acc = json.loads(epoch_result["data"])
                        y1.append(acc)
                num_point = len(y1)
                x = range(num_point)
                plt.plot(x, y1, curve_color, linewidth=1)

plt_curve(file_dir='TPE/experiment.json', curve_color="k") # black
plt_curve(file_dir='BOHB/experiment.json', curve_color="g") # green
plt_curve(file_dir='Hyperband/experiment.json', curve_color="b") # blue
plt_curve(file_dir='Random/experiment.json', curve_color="r") #red

plt.show()

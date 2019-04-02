import json
import matplotlib.pyplot as plt
import numpy as np

with open("repeated/BOHB_12h_3con_1GPU_paper/0.9938.json", encoding='utf-8') as f:
    data = json.load(f)

    for trials in data["trialMessage"]:
        hyperParameters = trials["hyperParameters"]
        _id = hyperParameters["parameter_id"]
        if _id[2] == '0':
            print("{\"s\":", _id[0], ", \"config\":", hyperParameters["parameters"], "},")

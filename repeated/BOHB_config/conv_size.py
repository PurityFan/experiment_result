import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from distutils.version import LooseVersion
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

with open("repeated/BOHB_config/usage.json", encoding='utf-8') as f:
    data = json.load(f)
    _x = []
    for params in data:
        conv_size = params["config"]["conv_size"] + 0
        _x.append(conv_size)
    
    X = np.concatenate((_x, []))[:, np.newaxis]

    X_plot = np.linspace(0, 10, 10000)[:, np.newaxis]

    fig, ax = plt.subplots()

    kde = KernelDensity(kernel='gaussian', bandwidth=0.1).fit(X)
    log_dens = kde.score_samples(X_plot)
    ax.plot(X_plot[:, 0], np.exp(log_dens), '-', label="conv_size range= '{0}'".format('[2, 3, 5, 7]'))

    ax.legend(loc='upper left')
    ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), '+k')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.7)
    plt.show()
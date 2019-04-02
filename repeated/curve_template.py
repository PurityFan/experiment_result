import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from distutils.version import LooseVersion
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

X = np.concatenate(([-1, -2, -1.5], [1,2,2,2,2,2, 5, 3]))[:, np.newaxis]

X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

fig, ax = plt.subplots()

kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(X)
log_dens = kde.score_samples(X_plot)
ax.plot(X_plot[:, 0], np.exp(log_dens), '-', label="kernel = '{0}'".format('gaussian'))

ax.legend(loc='upper left')
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), '+k')

ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)
plt.show()
"""
Visualization sets for the simulation
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(data_list, color, bins=10):
    data = np.array(data_list)
    data = data / 1000
    return plt.hist(data, bins=bins, color=color)

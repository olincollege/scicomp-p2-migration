"""
Visualization sets for the simulation
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(data_list, color, bins=10):
    data = np.array(data_list)
    data = data / 1000
    return plt.hist(data, bins=bins, color=color)


def compound_histogram(jeans_data, cold_data, photo_data, bins=10):
    jeans_data = np.array(jeans_data) / 1000
    cold_data = np.array(cold_data) / 1000
    photo_data = np.array(photo_data) / 1000
    plt.hist(jeans_data, bins=bins, color="red")
    plt.hist(cold_data, bins=bins, color="blue")
    plt.hist(photo_data, bins=bins, color="green")
    return plt.legend(["Jeans Escape", "Cold Trap", "Photodestruction"])

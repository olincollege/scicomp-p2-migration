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


def bar_plot(jeans_data, cold_data, photo_data):
    jeans_data = np.array(jeans_data) / 1000
    cold_data = np.array(cold_data) / 1000
    photo_data = np.array(photo_data) / 1000
    bars = [jeans_data, cold_data, photo_data]
    bar_labels = ["Jeans Escape", "Cold Trap", "Photodestruction"]
    bar_colors = ["tab:red", "tab:blue", "tab:green"]
    return plt.bar(bar_labels, bars, color=bar_colors)


def stacked_bar_plot(jeans_data, cold_data, photo_data):
    jeans_data = np.array(jeans_data) / 1000
    cold_data = np.array(cold_data) / 1000
    photo_data = np.array(photo_data) / 1000
    plt.bar("Percentages", photo_data, color="green")
    plt.bar("Percentages", cold_data, bottom=photo_data, color="blue")
    return plt.bar("Percentages", jeans_data, bottom=cold_data, color="red")

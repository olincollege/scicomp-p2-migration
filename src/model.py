"""
Visualization sets for the simulation
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def plot_histogram(data_list, color, bins=10):
    """
    Plot a histogram distribution

    Args:
        data_list: (list) A list of data points for the number of volatiles lost in a
        specific method
        color: (str) A string for the color to use for the graphs
        bins: (int) The number of bins to use for the distribution

    Returns:
        A histogram plot to use for the data
    """
    data = np.array(data_list)
    data = data / 1000
    return plt.hist(data, bins=bins, color=color)


def compound_histogram(jeans_data, cold_data, photo_data, bins=10):
    """
    Plot all histogram distributions for all volatile loss mechanisms

    Args:
        jeans_data: (list) A list integers for the number of volatiles lost by Jeans escape
        in a simulation
        cold_data: (list) A list integers for the number of volatiles lost by cold traps
        in a simulation
        photo_data: (list) A list integers for the number of volatiles lost by photodestruction
        in a simulation
        bins: (int) The number of bins to use for the distribution

    Returns:
        A plot containing three histograms of data used for the simulation
    """
    jeans_data = np.array(jeans_data) / 1000
    cold_data = np.array(cold_data) / 1000
    photo_data = np.array(photo_data) / 1000
    plt.hist(jeans_data, bins=bins, color="red")
    plt.hist(cold_data, bins=bins, color="blue")
    plt.hist(photo_data, bins=bins, color="green")
    return plt.legend(["Jeans Escape", "Cold Trap", "Photodestruction"])


def bar_plot(jeans_data, cold_data, photo_data):
    """
    Plot a set of bars for the average number of volatiles lost

    Args:
        jeans_data: (float) The average number of volatiles lost by Jeans escape
        in a simulation
        cold_data: (float) The average number of volatiles lost by cold traps
        in a simulation
        photo_data: (float) The average number of volatiles lost by photodestruction
        in a simulation

    Returns:
        A plot containing three bars containing the percentage of molecules
        lost by a specific mechanism
    """
    jeans_data = np.array(jeans_data) / 1000
    cold_data = np.array(cold_data) / 1000
    photo_data = np.array(photo_data) / 1000
    bars = [jeans_data, cold_data, photo_data]
    bar_labels = ["Jeans Escape", "Cold Trap", "Photodestruction"]
    bar_colors = ["tab:red", "tab:blue", "tab:green"]
    return plt.bar(bar_labels, bars, color=bar_colors)


def stacked_bar_plot(jeans_data, cold_data, photo_data):
    """
    Plot a stacked bar graph for the average number of volatiles lost

    Args:
        jeans_data: (float) The average number of volatiles lost by Jeans escape
        in a simulation
        cold_data: (float) The average number of volatiles lost by cold traps
        in a simulation
        photo_data: (float) The average number of volatiles lost by photodestruction
        in a simulation

    Returns:
        A plot containing a stacked bar containing the percentage of molecules
        lost by a specific mechanism
    """
    jeans_data = np.array(jeans_data) / 1000
    cold_data = np.array(cold_data) / 1000
    photo_data = np.array(photo_data) / 1000
    plt.bar("Percentages", photo_data, color="green")
    plt.bar("Percentages", cold_data, bottom=photo_data, color="blue")
    return plt.bar("Percentages", jeans_data, bottom=cold_data, color="red")


def pie_plot(jeans_data, cold_data, photo_data):
    """
    Plot a pie chart for the loss mechanism data

    Args:
        jeans_data: (float) The average number of volatiles lost by Jeans escape
        in a simulation
        cold_data: (float) The average number of volatiles lost by cold traps
        in a simulation
        photo_data: (float) The average number of volatiles lost by photodestruction
        in a simulation

    Returns:
        A plot containing a pie chart containing the percentage of molecules
        lost by a specific mechanism
    """
    data = [jeans_data, cold_data, photo_data]
    labels = ["Jeans Escape", "Cold Trap", "Photodestruction"]
    explode = (0, 0.2, 0.1)
    return plt.pie(
        data,
        explode=explode,
        labels=labels,
        autopct="%1.1f%%",
        colors=["red", "blue", "green"],
    )


def point_cloud(jeans_phi, jeans_theta, cold_phi, cold_theta, photo_phi, photo_theta):
    """
    Plot a point cloud around the surface of Mercury

    Args:
        jeans_data: (float) The average number of volatiles lost by Jeans escape
        in a simulation
        cold_data: (float) The average number of volatiles lost by cold traps
        in a simulation
        photo_data: (float) The average number of volatiles lost by photodestruction
        in a simulation

    Returns:
        A 3D plot containing a spherical plot of Mercury as well as colored points for where
        a molecule was last located before being lost
    """
    radius_mercury = 1
    radius_point_cloud = 1.3
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0.0:pi:100j, 0.0 : 2.0 * pi : 100j]
    x = radius_mercury * sin(phi) * cos(theta)
    y = radius_mercury * sin(phi) * sin(theta)
    z = radius_mercury * cos(phi)

    x_jeans = radius_point_cloud * sin(jeans_phi) * cos(jeans_theta)
    y_jeans = radius_point_cloud * sin(jeans_phi) * sin(jeans_theta)
    z_jeans = radius_point_cloud * cos(jeans_phi)

    x_cold = radius_point_cloud * sin(cold_phi) * cos(cold_theta)
    y_cold = radius_point_cloud * sin(cold_phi) * sin(cold_theta)
    z_cold = radius_point_cloud * cos(cold_phi)

    x_photo = radius_point_cloud * sin(photo_phi) * cos(photo_theta)
    y_photo = radius_point_cloud * sin(photo_phi) * sin(photo_theta)
    z_photo = radius_point_cloud * cos(photo_phi)

    ax = plt.axes(projection="3d")
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color="c", alpha=0.3, linewidth=0)
    ax.scatter(x_jeans, y_jeans, z_jeans, color="red")
    ax.scatter(x_cold, y_cold, z_cold, color="blue")
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_zlabel("Z-Axis")
    return ax.legend(["Mercury", "Jeans Escape", "Cold Traps"])

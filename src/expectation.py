"""
Calculate statistical parameters of every simulation run
"""
import numpy as np
from src.agents import Volatile


def simulate(runs, simulations):
    """
    Runs the simulation a certain number of times

    Args:
        runs: (int) The number of hops the volatiles in the simulation will make
        simulations: (int) The number of times to run the simulation

    Returns:
        A list of statisitcs for the photodestruction, cold traps, and jeans escape as well as the
        final results of a randomly selected simulation
    """
    photo_stats = []
    cold_stats = []
    jean_stats = []
    random_selection = np.random.randint(0, simulations)

    for i in range(simulations):
        volatiles = Volatile()
        for j in range(runs):
            volatiles.migrate(2.989e-26)
        if i == random_selection:
            cold_phi = volatiles.cold_phi
            cold_theta = volatiles.cold_theta
            jeans_phi = volatiles.jeans_phi
            jeans_theta = volatiles.jeans_theta
            photo_phi = volatiles.photo_phi
            photo_theta = volatiles.photo_theta

        # We must subtract by 1 since there is a dummy value at the beginning of each array
        photo_stats.append(len(volatiles.photo_phi) - 1)
        cold_stats.append(len(volatiles.cold_phi) - 1)
        jean_stats.append(len(volatiles.jeans_phi) - 1)
    return (
        photo_stats,
        cold_stats,
        jean_stats,
        cold_phi,
        cold_theta,
        jeans_phi,
        jeans_theta,
        photo_phi,
        photo_theta,
    )


def calculate_statistics(volatile_list: list):
    """
    Calculates the trajectory velocity of a given volatile

    Args:
        volatile_list: (list) A list of results from the simulation of how many
        molecules were lost

    Returns:
        The initial launch velocity of the particle
    """

    quantity_mean = np.mean(volatile_list)
    quantity_median = np.median(volatile_list)
    quantity_std = np.std(volatile_list)
    return quantity_mean, quantity_median, quantity_std


def statistical_significance(volatile_list, mean):
    """
    Calculates the statistical significance of the data

    Args:
        volatile_list: null
        mean: (float) The given mean of the volatiles landing in cold spots as denoted by the paper

    Returns:
        The respective t-value of the simulation
    """

    test_mean, test_median, test_std = calculate_statistics(volatile_list)
    t_value = (test_mean - mean) / (test_std / (50) ** 0.5)
    return t_value, test_median

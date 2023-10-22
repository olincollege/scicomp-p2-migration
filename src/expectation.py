"""
Calculate statistical parameters of every simulation run
"""
import numpy as np
from src.agents import Volatile


def simulate(runs):
    volatiles = Volatile()
    for j in range(runs):
        volatiles.migrate(2.989e-26)


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


def lattitude_distribution(phi):
    """
    Creates a distribution for the lattitude of the particles that landed in cold spots

    Args:
        phi: (list) The given lattitude of a particle that landed in a cold trap in radians

    Returns:
        A binned distribution of where each particle landed (Should resemble
        the a Beta of the Mercury for the percentage of the lattitude measurements)
    """
    return np.histogram(phi)


def statistical_significance(volatile_list):
    """
    Null docstring

    Args:
        volatile_list: null

    Returns:
        null
    """

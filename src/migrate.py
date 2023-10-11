"""
Migration derivations for volatile migrations
"""
import numpy as np
import src.helpers as kine

PHOTO_WATER = 1.0 * 10**4
PHOTO_CARBON_DIOXIDE = 3.3 * 10**4


def cold_trap(temperature):
    """
    Null docstring

    Args:
        null

    Returns:
        null
    """
    if temperature <= kine.COLD_TRAP:
        return True
    return False


def jeans_escape(velocity, emergent_angle):
    """
    Null docstring

    Args:
        null

    Returns:
        null
    """
    vert_velocity = float(velocity * np.sin(emergent_angle))
    if vert_velocity <= kine.ESC_MERCURY:
        return True
    return False


def photodestruction(volatile, time):
    """
    Null docstring

    Args:
        null

    Returns:
        null
    """
    pass

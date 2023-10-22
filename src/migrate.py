"""
Migration derivations for volatile migrations
"""
import numpy as np
import src.helpers as kine
from scipy.sparse import find as spf

# Photodestruction Constants
PHOTO_WATER = 1.0e4  # 10^4 Seconds
PHOTO_CARBON_DIOXIDE = 3.3e4  # 3.3 * 10^4 Seconds


def volatile_loss(
    temperature,
    velocity,
    emergent_angle,
    time,
    volatile="water",
):
    """
    Find out if a volatile has been lost

    Args:
        temperature: (float) The temperature of a volatile in Kelvin
        velocity: (float) The magnitude of the initial trajectory
        velocity in meters per second
        emergent_angle: (float) The launch angle in radians off of the
        ground when the volatile jumps
        time: (float) The amount of time in seconds a volatile
        will remain in the air for a jump
        volatile: (string) The specified volatile used in the simulation
        (Set to water by default)

    Returns:
        A list of booleans for whether or not a volatile is lost
    """
    return (
        jeans_escape(velocity, emergent_angle),
        cold_trap(temperature),
        photodestruction(time, volatile),
    )


def cold_trap(temperature):
    """
    Determine whether or not the volatile steps into the territory of a
    cold trap

    Args:
        temperature: (float) The temperature of a volatile in Kelvin

    Returns:
        A Boolean statement for when the volatile should be taken out of the
        simulation space by cold trap
    """
    sparse_indicies = spf(temperature <= kine.COLD_TRAP)
    return temperature <= kine.COLD_TRAP


def jeans_escape(velocity, emergent_angle):
    """
    Determine whether or not the volatile escapes the atmosphere due
    to Jeans' escape

    Args:
        velocity: (float) The magnitude of the initial trajectory
        velocity in meters per second
        emergent_angle: (float) The launch angle in radians off of the
        ground when the volatile jumps

    Returns:
        A Boolean statement for when the volatile should be taken out of the
        simulation space by exceeding the escape velocity
    """
    vert_velocity = velocity * np.sin(emergent_angle)
    return vert_velocity >= kine.ESC_MERCURY


def photodestruction(time, volatile="water"):
    """
    Determine whether or not the volatile cannot continue in the
    simulation due to photodestruction

    Args:
        time: (float) The amount of time in seconds a volatile
        will remain in the air for a jump
        volatile: (string) The specified volatile used in the simulation
        (Set to water by default)

    Returns:
        A Boolean statement for when the volatile should be taken out of the
        simulation space by photodestruction
    """
    if volatile == "water":
        timescale = PHOTO_WATER
    elif volatile == "carbon_dioxide":
        timescale = PHOTO_CARBON_DIOXIDE
    else:
        timescale = PHOTO_WATER
    probability_factor = 1 - np.exp(-1 * (time / timescale))
    probability = np.random.rand(1)
    return probability < probability_factor

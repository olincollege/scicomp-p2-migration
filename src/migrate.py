"""
Migration derivations for volatile migrations
"""
import numpy as np
from scipy.sparse import find as spf
import src.helpers as kine

# Photodestruction Constants
PHOTO_WATER = 1.0e4  # 10^4 Seconds
PHOTO_CARBON_DIOXIDE = 3.3e4  # 3.3 * 10^4 Seconds


def volatile_loss(
    temperature,
    velocity,
    emergent_angle,
    time,
    phi,
    theta,
    jeans_phi,
    jeans_theta,
    cold_phi,
    cold_theta,
    photo_phi,
    photo_theta,
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
        phi: (float) The set of free particle's lattitude angle
        theta: (float) The set of free particle's longitude angle
        volatile: (string) The specified volatile used in the simulation
        (Set to water by default)

    Returns:
        A list of booleans for whether or not a volatile is lost
    """

    # First check to see if the volatile has exceeded the vertical
    # escape velocity of Mercury (Jeans escape)

    jeans_phi, jeans_theta, time, temperature, phi, theta = jeans_escape(
        velocity,
        emergent_angle,
        temperature,
        time,
        phi,
        theta,
        jeans_phi,
        jeans_theta,
    )

    # Next check to see if the volatile has migrated to a cold
    # trap

    cold_phi, cold_theta, time, phi, theta = cold_trap(
        temperature, time, phi, theta, cold_phi, cold_theta
    )

    # Finally, check to see if the volatile has encounter photodestruction
    photo_phi, photo_theta, phi, theta = photodestruction(
        time, phi, theta, photo_phi, photo_theta, volatile
    )
    return (
        phi,
        theta,
        jeans_phi,
        jeans_theta,
        cold_phi,
        cold_theta,
        photo_phi,
        photo_theta,
    )


def cold_trap(temperature, time, phi, theta, cold_phi, cold_theta):
    """
    Determine whether or not the volatile steps into the territory of a
    cold trap

    Args:
        temperature: (float) The temperature of a volatile in Kelvin

    Returns:
        A Boolean statement for when the volatile should be taken out of the
        simulation space by cold trap
    """
    sparse_indicies = list(spf(temperature <= kine.COLD_TRAP))[1]
    cold_phi = np.concatenate((cold_phi, np.take(phi, sparse_indicies, axis=0)))
    cold_theta = np.concatenate((cold_theta, np.take(theta, sparse_indicies, axis=0)))
    phi = np.delete(phi, sparse_indicies)
    theta = np.delete(theta, sparse_indicies)
    time = np.delete(time, sparse_indicies)
    return cold_phi, cold_theta, time, phi, theta


def jeans_escape(
    velocity,
    emergent_angle,
    temperature,
    time,
    phi,
    theta,
    jeans_phi,
    jeans_theta,
):
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
    sparse_indicies = list(spf(vert_velocity >= kine.ESC_MERCURY))[1]
    jeans_phi = np.concatenate((jeans_phi, np.take(phi, sparse_indicies, axis=0)))
    jeans_theta = np.concatenate((jeans_theta, np.take(theta, sparse_indicies, axis=0)))
    phi = np.delete(phi, sparse_indicies)
    theta = np.delete(theta, sparse_indicies)
    time = np.delete(time, sparse_indicies)
    temperature = np.delete(temperature, sparse_indicies)
    return jeans_phi, jeans_theta, time, temperature, phi, theta


def photodestruction(time, phi, theta, photo_phi, photo_theta, volatile="water"):
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
    probability = np.random.rand(np.size(time, axis=0))
    sparse_indicies = list(spf(probability < probability_factor))[1]
    photo_phi = np.concatenate((photo_phi, np.take(phi, sparse_indicies, axis=0)))
    photo_theta = np.concatenate((photo_theta, np.take(theta, sparse_indicies, axis=0)))
    phi = np.delete(phi, sparse_indicies)
    theta = np.delete(theta, sparse_indicies)
    return photo_phi, photo_theta, phi, theta

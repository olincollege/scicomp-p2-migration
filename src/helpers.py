"""
Initial and Nonvariable Condition setting and PDF allocation
"""

import numpy as np

# Note: All units have been converted into SI Units
BOLTZMANN_CONSTANT = 1.38 * 10 ** (-23)  # 1.38 * 10^-23 J/K
RAD_MERCURY = 2.439 * 10**6  # 2,439 km
GRAV_MERCURY = 3.705  # 3.705 m/s^2
ESC_MERCURY = 4.251 * 10**3  # 4.251 km/s
SURFACE_TEMPERATURE = 1.381 * 10**2  # 138.1 K
TERMINATOR_MERCURY = 3.785 * 10**2  # 378.5 K
N = 3.7 * 10 ** (-1)  # Run Parameter
WATER_MASS = 2.989 * 10 ** (-26)  # 18.02 amuK
CARBON_DIOXIDE_MASS = 7.308 * 10 ** (-26)  # 44.01 amu
COLD_TRAP = 225  # 225 K
NEWTON_CONSTANT = 6.67 * 10 ** (-11)  # 6.67 * 10^-11 m^3 / kg s^2


def molecule_temperature(phi):
    """
    Calculates the temperature of a select volatile in the
    simulation space

    Args:
        phi: (float) The given altitudal angle of a particle on the
        surface of the planet

    Returns:
        The temperature of a given particle
    """

    mole_temp = SURFACE_TEMPERATURE + TERMINATOR_MERCURY * float(
        np.cos(phi - (np.pi / 2)) ** N
    )
    return mole_temp


def launch_velocity(temperature, volatile):
    """
    Calculates the velocity of a particle on temperature
    dependence

    Args:
        temperature: (float) The temperature of a given molecule
        in Kelvin
        volatile: (int) A number, either 0 or 1, that indicates
        if the molecule used in the simulation is water or
        carbon dioxide

    Returns:
        The emergent launch velocity in meters per second
    """
    if volatile == 0:
        return (3 * BOLTZMANN_CONSTANT * temperature / WATER_MASS) ** 0.5
    return (3 * BOLTZMANN_CONSTANT * temperature / CARBON_DIOXIDE_MASS) ** 0.5


def emergent_angle():
    """
    Calculates the angle in reference to the ground of the simulation

    Returns:
        The angle (psi) that the volatile launches at
    """

    return np.random.uniform(0, np.pi / 2)

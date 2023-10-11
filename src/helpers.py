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
WATER_MASS = 2.989 * 10 ** (-26)  # 18.02 amu
CARBON_DIOXIDE_MASS = 7.308 * 10 ** (-26)  # 44.01 amu
COLD_TRAP = 225  # 225 K
NEWTON_CONSTANT = 6.67 * 10 ** (-11)  # 6.67 * 10^-11 m^3 / kg s^2


def pdf_velocity(temperature, mass):
    """
    Calculates the trajectory velocity of a given volatile

    Args:
        temperature: (float) The given temperature of a specific
        area within the simulation space
        mass: (float) The specific particle mass in kilograms
        of a specific volatile

    Returns:
        The initial launch velocity of the particle
    """
    # The following pdf has been rederived to map the given pdf function
    # by calculating the expectation values to find velociy uncertainty
    # the calculation is explained in further depth in the Jupyter notebook

    calc_velocity = (3 * BOLTZMANN_CONSTANT * temperature / mass) ** 0.5
    volatile_speed = np.random.normal(calc_velocity, calc_velocity)
    # Handles the potential case of the velocity being less than zero
    return max(volatile_speed, 0)


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


def adjusted_gravity(height):
    """
    Calculates the adjusted gravity constant in a simulation
    where gravity varies

    Args:
        height: (float) The maximum height in meters attained
        in the simulation a volatile would move at under regular
        gravity

    Returns:
        The approximated gravitational constant under variable
        gravity
    """

    # Note: This is only an approximation for the change in gravity
    # the resulting differential equation is nonhomogenous and difficult
    # to solve. If I have enough time and would like to make the model
    # more accurate, I'll implement Runge-Kutta for a more accurate
    # trajectory mapping

    return GRAV_MERCURY * (RAD_MERCURY / (RAD_MERCURY + height)) ** 2


def max_height(velocity, incidence, gravity=GRAV_MERCURY):
    """
    Calculates the maximum height achieved by a volatile

    Args:
        velocity: (float) The intial velocity of a volatile when
        leaping in m/s
        incidence: (float) The angle at which the volatile will hop
        at in radians
        gravity: (float) The approximation of gravity causing a parabolic
        trajectory in m/s (Set to the acceleration on ground level
        on Mercury by default)

    Returns:
        The maximum height achieved in meters achieved by a volatile
    """

    velocity_y_squared = (velocity * np.sin(incidence)) ** 2
    return (RAD_MERCURY * velocity_y_squared) / (
        2 * RAD_MERCURY * gravity - velocity_y_squared
    )


def calc_distance(velocity, incidence, gravity=GRAV_MERCURY):
    """
    Calculates the displacement of a volatile

    Args:
        velocity: (float) The intial velocity of a volatile when
        leaping in m/s
        incidence: (float) The angle at which the volatile will hop
        at in radians
        gravity: (float) The approximation of gravity causing a parabolic
        trajectory in m/s (Set to the acceleration on ground level
        on Mercury by default)

    Returns:
        The maximum height achieved in meters achieved by a volatile
    """
    velocity_x = velocity * np.cos(incidence)
    velocity_y = velocity * np.sin(incidence)
    time = 2 * velocity_y / gravity
    return velocity_x * time


def calc_radians(displacement):
    """
    Calculates the distance traveled by the molecule in radians

    Args:
        displacement: (float) The kinematic distance in meters traveled
        by the volatile

    Returns:
        The amount of distance traveled by the particle as a radian
        equivalent on the position of the sphere.
    """
    return displacement / RAD_MERCURY

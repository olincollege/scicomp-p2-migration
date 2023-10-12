"""
Defines a volatile agent utilized in the model
"""
import numpy as np
import helpers as helper
from src.migrate import volatile_loss

RADIUS = helper.RAD_MERCURY


class Volatile:

    """
    Define characteristics for a volatile molecule that migrates
    along the surface of Mercury
    """

    def __init__(self):
        self.theta = np.random.uniform(0, 2 * np.pi)
        self.phi = np.random.uniform(0, np.pi)
        self.temperature = helper.molecule_temperature(self.phi)
        self.emergent_angle = helper.emergent_angle()
        self.velocity = 0
        self.time = 0
        self.loss = [False, False, False]

    def migrate(self, mass: float):
        """
        Allow 1 volatile to undergo a hop in the simulation

        Args:
            mass: (float) The specific particle mass in kilograms
            of a specific volatile
        """
        if self.loss[0] is True:
            pass
        elif self.loss[1] is True:
            pass
        elif self.loss[2] is True:
            pass
        else:
            self.temperature = helper.molecule_temperature(self.phi)
            self.velocity = pdf_velocity(self.temperature, mass)
            self.emergent_angle = helper.emergent_angle()
            height = helper.max_height(self.velocity, self.emergent_angle)
            self.time = flight_time(self.velocity, self.emergent_angle, height)
            distance = helper.calc_distance(self.velocity, self.emergent_angle)
            radians = helper.calc_radians(distance)
            heading = heading_direction()
            self.calc_heading(radians, heading)
            self.loss = volatile_loss(
                self.temperature, self.velocity, self.emergent_angle, self.time
            )

    def calc_heading(self, arc: float, heading: float):
        """
        Calculate the new position of a volatile

        Args:
            arc: (float) The length of the arc mapped on a sphere a particle
            travels at
            heading: The angle at which a volatile heads
        """
        self.phi = (self.phi + arc * np.sin(heading)) % np.pi
        self.theta = (self.theta + arc * np.cos(heading)) % 2 * np.pi


def heading_direction():
    """
    Calculates the direction on the sphere the volatile goes in

    Returns:
        T The angle at which the volatile travels to as a unit vector
    """
    return float(np.random.uniform(0, 2 * np.pi))


def pdf_velocity(temperature: float, mass: float):
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

    calc_velocity = (3 * helper.BOLTZMANN_CONSTANT * temperature / mass) ** 0.5
    volatile_speed = np.random.normal(calc_velocity, calc_velocity)
    # Handles the potential case of the velocity being less than zero
    return max(float(volatile_speed), 0)


def flight_time(
    velocity: float,
    incidence: float,
    h_max: float,
    gravity: float = helper.GRAV_MERCURY,
):
    """
    Calculate the time of flight for a volatile of a given maximum
    height

    Args:
        velocity: (float) The intial velocity of a volatile when
        leaping in m/s
        incidence: (float) The angle at which the volatile will hop
        at in radians
        h_max: (float) The maximum height in meters that the volatile
        reaches in its trajectory
        gravity: (float) The approximation of gravity causing a parabolic
        trajectory in m/s (Set to the acceleration on ground level
        on Mercury by default)

    Returns:
        The amount of time the volatile spends in the air
    """
    vel_y = float(velocity * np.sin(incidence))
    a = RADIUS * vel_y**2
    b = vel_y**2 - 2 * gravity * RADIUS
    u_0 = a
    u_f = a + b * h_max
    v_0 = RADIUS
    v_f = RADIUS + h_max
    l = a - b * RADIUS
    p_0 = (a + b * RADIUS) / l
    p_f = (2 * b * h_max + a + b * RADIUS) / l

    def eval_integral(p, u, v):
        """
        Place in the limits of integrations of the flight
        time integral detailed in the paper
        """
        return float((np.sqrt(u * v) / b)) + (l / (2 * b)) * float(
            (1 / np.sqrt(-b))
        ) * float(np.arcsin(p))

    return 2 * (eval_integral(p_f, u_f, v_f) - eval_integral(p_0, u_0, v_0))

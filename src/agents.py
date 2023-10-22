"""
Defines a volatile agent utilized in the model
"""
import numpy as np
import src.helpers as helper
from src.migrate import volatile_loss

RADIUS = helper.RAD_MERCURY
N_MOLECULE = 100000

np.random.seed(299)


class Volatile:

    """
    Define characteristics for a volatile molecule that migrates
    along the surface of Mercury
    """

    def __init__(self):
        """
        Set up the initial volatile characteristics that define important
        features of the volatile
        """
        self.theta = np.random.rand(N_MOLECULE) * 2 * np.pi
        self.phi = np.arccos(1 - 2 * np.random.rand(N_MOLECULE))
        self.temperature = helper.molecule_temperature(self.phi)
        self.emergent_angle = np.array(
            [helper.emergent_angle() for i in range(N_MOLECULE)]
        )
        self.velocity = np.zeros(N_MOLECULE, dtype=float)
        self.time = np.zeros(N_MOLECULE, dtype=float)
        self.photo_phi = np.zeros(1)
        self.photo_theta = np.zeros(1)
        self.jeans_phi = np.zeros(1)
        self.jeans_theta = np.zeros(1)
        self.cold_phi = np.zeros(1)
        self.cold_theta = np.zeros(1)

    def migrate(self, mass: float):
        """
        Allow 1 volatile to undergo a hop in the simulation

        Args:
            mass: (float) The specific particle mass in kilograms
            of a specific volatile
        """

        # If the volatile hasn't been lost, then calculate where the volatile
        # will then end up as well as it's temperature and flight time
        # to find out if the volatile becomes lost in the next iteration
        self.temperature = helper.molecule_temperature(self.phi)
        self.velocity = pdf_velocity(self.temperature, mass)
        self.emergent_angle = helper.emergent_angle()
        height = helper.max_height(self.velocity, self.emergent_angle)
        adj_gravity = helper.adjusted_gravity(height)
        self.time = flight_time(self.velocity, self.emergent_angle, adj_gravity)
        distance = helper.calc_distance(self.velocity, self.emergent_angle, adj_gravity)
        radians = helper.calc_radians(distance)
        heading = heading_direction()
        self.calc_heading(radians, heading)
        (
            self.phi,
            self.theta,
            self.jeans_phi,
            self.jeans_theta,
            self.cold_phi,
            self.cold_theta,
            self.photo_phi,
            self.photo_theta,
        ) = volatile_loss(
            self.temperature,
            self.velocity,
            self.emergent_angle,
            self.time,
            self.phi,
            self.theta,
            self.jeans_phi,
            self.jeans_theta,
            self.cold_phi,
            self.cold_theta,
            self.photo_phi,
            self.photo_theta,
        )

    def calc_heading(self, arc, heading):
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
        The angle at which the volatile travels to as a unit vector
    """
    return np.random.uniform(0, 2 * np.pi)


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

    calc_velocity = (3 * helper.BOLTZMANN_CONSTANT * temperature / mass) ** 0.5
    volatile_speed = np.random.normal(calc_velocity, calc_velocity)
    # Handles the potential case of the velocity being less than zero
    return abs(volatile_speed)


def flight_time(
    velocity,
    incidence,
    gravity=helper.GRAV_MERCURY,
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
    vel_y = velocity * np.sin(incidence)
    return vel_y / gravity

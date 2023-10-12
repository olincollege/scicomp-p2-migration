"""
Defines a volatile agent utilized in the model
"""
import numpy as np
import helpers as helper
from src.migrate import volatile_loss


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

    def migrate(self, mass):
        """
        Allow 1 volatile to undergo a hop in the simulation
        """
        if self.loss[0] is True:
            pass
        elif self.loss[1] is True:
            pass
        elif self.loss[2] is True:
            pass
        else:
            self.temperature = helper.molecule_temperature(self.phi)
            self.velocity = helper.pdf_velocity(self.temperature, mass)
            self.emergent_angle = helper.emergent_angle()
            height = helper.max_height(self.velocity, self.emergent_angle)
            self.time = helper.flight_time(self.velocity, self.emergent_angle, height)
            self.loss = volatile_loss(
                self.temperature, self.velocity, self.emergent_angle, self.time
            )

    def heading_direction(self):
        """
        Calculates the direction on the sphere the volatile goes in
        """
        return float(np.random.uniform(0, 2 * np.pi))

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

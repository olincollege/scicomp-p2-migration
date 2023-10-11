"""
Defines a volatile agent utilized in the model
"""
import numpy as np
import helpers as helper


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
        self.heading = 0
        self.velocity = 0

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

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


x = Volatile()
print(x)
print(x.theta)
print(x.phi)
print(x.temperature)
print(x.emergent_angle)

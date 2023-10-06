"""
Defines a volatile agent utilized in the model
"""


class Volatile:

    """
    Define characteristics for a volatile molecule that migrates
    along the surface of Mercury
    """

    def __init__(self) -> None:
        self.temperature = 0
        self.theta = 0
        self.phi = 0
        self.emergent_angle = 0

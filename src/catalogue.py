import numpy as np


def generate_random_catalogue(n_galaxies=1000, box_size=1000):
    """
    Generate a random galaxy catalogue inside a cubic box.

    Parameters
    ----------
    n_galaxies : int
        Number of galaxies to generate.
    box_size : float
        Size of the cubic box in Mpc/h.

    Returns
    -------
    positions : ndarray
        Array of shape (n_galaxies, 3) containing x, y, z positions.
    """

    positions = np.random.uniform(
        0, box_size, size=(n_galaxies, 3)
    )

    return positions

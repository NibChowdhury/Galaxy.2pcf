import numpy as np


def pair_separations(positions):
   

    separations = []

    n_galaxies = len(positions)

    for i in range(n_galaxies):
        for j in range(i + 1, n_galaxies):

            separation = np.linalg.norm(
                positions[i] - positions[j]
            )

            separations.append(separation)

    return np.array(separations)

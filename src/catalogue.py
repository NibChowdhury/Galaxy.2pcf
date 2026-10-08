import numpy as np


def generate_random_catalogue(n_galaxies=1000, box_size=1000):
   

    positions = np.random.uniform(
        0, box_size, size=(n_galaxies, 3)
    )
def generate_clustered_catalogue(
    n_galaxies=1000,
    n_clusters=50,
    box_size=1000.0,
    cluster_size=20.0
):
   
    cluster_centres = np.random.uniform(
        0,
        box_size,
        size=(n_clusters, 3)
    )

    cluster_indices = np.random.randint(
        0,
        n_clusters,
        size=n_galaxies
    )

    positions = (
        cluster_centres[cluster_indices]
        + np.random.normal(
            0,
            cluster_size,
            size=(n_galaxies, 3)
        )
    )

    positions %= box_size
    return positions

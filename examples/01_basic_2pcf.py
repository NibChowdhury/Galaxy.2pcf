import numpy as np

from src.catalogue import (
    generate_random_catalogue,
    generate_clustered_catalogue
)

from src.pair_counts import pair_separations
from src.correlation import pair_counts


n_galaxies = 1000
box_size = 1000.0  # Mpc/h


random_galaxies = generate_random_catalogue(
    n_galaxies=n_galaxies,
    box_size=box_size
)

clustered_galaxies = generate_clustered_catalogue(
    n_galaxies=n_galaxies,
    n_clusters=50,
    box_size=box_size,
    cluster_size=20.0
)


random_separations = pair_separations(
    random_galaxies
)

clustered_separations = pair_separations(
    clustered_galaxies
)

bins = np.logspace(
    np.log10(1.0),
    np.log10(500.0),
    20
)


RR = pair_counts(
    random_separations,
    bins
)

DD = pair_counts(
    clustered_separations,
    bins
)



print("Number of galaxies:", n_galaxies)

print(
    "Number of random pairs:",
    len(random_separations)
)

print(
    "Number of clustered pairs:",
    len(clustered_separations)
)

print("\nSeparation bins:")
print(bins)

print("\nRR(r) - random pair counts:")
print(RR)

print("\nDD(r) - clustered pair counts:")
print(DD)

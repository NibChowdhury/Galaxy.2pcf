import numpy as np

from src.catalogue import generate_random_catalogue
from src.pair_counts import pair_separations
from src.correlation import pair_counts

n_galaxies = 1000
box_size = 1000.0  # Mpc/h

galaxies = generate_random_catalogue(
    n_galaxies=n_galaxies,
    box_size=box_size
)


separations = pair_separations(galaxies)


bins = np.logspace(
    np.log10(1.0),
    np.log10(500.0),
    20
)


DD = pair_counts(
    separations,
    bins
)


print("Number of galaxies:", n_galaxies)
print("Number of galaxy pairs:", len(separations))

print("\nSeparation bins:")
print(bins)

print("\nDD(r) pair counts:")
print(DD)

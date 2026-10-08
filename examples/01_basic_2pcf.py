import numpy as np
import matplotlib.pyplot as plt

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


random_separations = pair_separations(random_galaxies)
clustered_separations = pair_separations(clustered_galaxies)

bins = np.logspace(
    np.log10(1.0),
    np.log10(500.0),
    20
)

r = 0.5 * (bins[1:] + bins[:-1])


RR = pair_counts(random_separations, bins)
DD = pair_counts(clustered_separations, bins)


print("Number of galaxies:", n_galaxies)
print("Number of random pairs:", len(random_separations))
print("Number of clustered pairs:", len(clustered_separations))


plt.figure(figsize=(8, 8))

plt.scatter(
    random_galaxies[:, 0],
    random_galaxies[:, 1],
    s=5,
    alpha=0.4,
    label="Random"
)

plt.scatter(
    clustered_galaxies[:, 0],
    clustered_galaxies[:, 1],
    s=5,
    alpha=0.4,
    label="Clustered"
)

plt.xlabel(r"$x\ [h^{-1}\mathrm{Mpc}]$")
plt.ylabel(r"$y\ [h^{-1}\mathrm{Mpc}]$")
plt.title("Synthetic Galaxy Catalogues")
plt.legend()
plt.tight_layout()

plt.savefig(
    "figures/galaxy_catalogues.png",
    dpi=300
)

plt.close()


plt.figure(figsize=(8, 6))

plt.plot(
    r,
    DD,
    marker="o",
    label="DD(r) — clustered"
)

plt.plot(
    r,
    RR,
    marker="o",
    label="RR(r) — random"
)

plt.xscale("log")
plt.yscale("log")

plt.xlabel(r"$r\ [h^{-1}\mathrm{Mpc}]$")
plt.ylabel("Pair counts")

plt.title("Galaxy Pair Counts")

plt.legend()
plt.tight_layout()

plt.savefig(
    "figures/pair_counts.png",
    dpi=300
)

plt.close()

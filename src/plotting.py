import matplotlib.pyplot as plt


def plot_correlation(r, xi):
  

    plt.figure(figsize=(8, 6))

    plt.plot(r, xi, marker="o")

    plt.axhline(0, linestyle="--")

    plt.xscale("log")

    plt.xlabel(r"$r$ [$h^{-1}$ Mpc]")
    plt.ylabel(r"$\xi(r)$")

    plt.title("Galaxy Two-Point Correlation Function")

    plt.tight_layout()

    plt.show()

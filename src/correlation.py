import numpy as np


def pair_counts(separations, bins):


    counts, _ = np.histogram(separations, bins=bins)

    return counts


def landy_szalay(DD, DR, RR):
    

    xi = (DD - 2.0 * DR + RR) / RR

    return xi

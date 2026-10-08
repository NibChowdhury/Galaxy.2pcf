# Galaxy.2pcf
Calculates the 2 point galaxy correlation function
A small Python project to measure the two-point correlation function of galaxies, to understand how galaxies cluster on different spatial scales. 
We have used a synthetic galaxy catalog which one can progressively build towards more realistic mock catalogs/observational galaxy samples. 
------------------------------------------------------------------------------------- 
# Overview

The two-point correlation function $\xi(r)$ describes the excess
probability of finding a pair of galaxies separated by a distance \( r \),
relative to a random distribution.

It is defined through

$$
dP = \bar{n}^{\,2}\,[1+\xi(r)]\,dV_1\,dV_2
$$

where $\bar{n}$ is the mean number density of galaxies.

In this project, we estimate the correlation function using the
Landy–Szalay estimator:

$$
\xi(r) =
\frac{DD(r)-2DR(r)+RR(r)}
{RR(r)}
$$

where:

- \(DD(r)\) = galaxy–galaxy pair counts
- \(DR(r)\) = galaxy–random pair counts
- \(RR(r)\) = random–random pair counts

For a completely random distribution, we expect approximately

$$
\xi(r) \approx 0
$$

while a positive value of $\xi(r)$ indicates an excess of galaxy
pairs at separation  $r$, corresponding to clustering.

#!/usr/bin/env python3

import numpy as np

# Extended Array Creation
a = np.linspace(0, 2*np.pi, 100)  # Values from 0 to 2π
b = np.logspace(1, 10, base=2, num=10)  # Values from 2^1 to 2^10
c = np.zeros((3, 3))  # 3x3 array of zeros
d = np.eye(4)  # 4x4 identity matrix
e = np.random.rand(4, 4)  # 4x4 array of random numbers

# Advanced Operations
f = np.dot(a, a)  # Dot product
g = np.cross(np.ones(3), np.arange(1, 4))  # Cross product
h = np.linalg.inv(d + e)  # Inverse of a matrix
i = np.fft.ifft(np.fft.fft(a))  # FFT and inverse FFT

# Random Number Generation
j = np.random.randint(1, 100, size=(10, 10))  # 10x10 array of random integers
k = np.random.choice(a, size=10)  # Random sample from 'a'

# Complex Operations
l = np.vander(np.arange(1, 6), increasing=True)  # Vandermonde matrix
m = np.linalg.eigvals(l)  # Eigenvalues of the Vandermonde matrix

# Boolean Indexing and Masking
n = a > np.pi  # Boolean mask for values greater than π
o = a[n]  # Apply mask

# Slicing and Dicing
p = j[::2, ::2]  # Every other element

# Statistical Operations
q = np.mean(j)  # Mean
r = np.std(b)  # Standard deviation
s = np.percentile(k, 50)  # Median (50th percentile)

# Stacking and Splitting
t = np.vstack((a[:50], a[50:]))  # Stack two halves of 'a' vertically
u, v = np.hsplit(t, 2)  # Split 't' horizontally

# Additional operations for broader coverage
structured_array = np.zeros((10,), dtype=[('x', 'i4'), ('y', 'f4')])  # Structured array
structured_array['x'] = np.arange(10)
structured_array['y'] = np.sin(np.arange(10))
complex_array = np.exp(2j * np.pi * np.arange(5) / 5)  # Complex numbers
structured_op = structured_array['x'] + structured_array['y']  # Operation on structured array

# Ensure usage of various random generators and operations
rng = np.random.default_rng()  # New default random number generator
for dist_name in ['normal', 'uniform', 'binomial']:
    if dist_name == 'binomial':
        # For binomial, n (number of trials) and p (success probability) must be provided
        sample = rng.binomial(n=10, p=0.5, size=5)
    elif dist_name == 'normal':
        sample = rng.normal(loc=0.0, scale=1.0, size=5)
    elif dist_name == 'uniform':
        sample = rng.uniform(low=0.0, high=1.0, size=5)
    print(f"Sample from {dist_name}: {sample}")

print("Eigenvalues of the Vandermonde matrix:", m)
print("Inverse of modified identity matrix (d+e):\n", h)
print("FFT and inverse FFT of 'a':\n", i)
print("Random integers in a 10x10 matrix:\n", j)
print("Completed an extensive demonstration of numpy functionalities.")

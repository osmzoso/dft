#!/usr/bin/env python
"""
Discrete Fourier Transform DFT
"""
import math


def dft(x):
    """
    Compute the Discrete Fourier Transform (DFT)

    Parameter x : The time-domain signal as a list of complex numbers.
    Returns   X : List of DFT coefficients (frequency-domain representation).
    """
    N = len(x)
    X = [complex()] * N
    for k in range(N):  # Loop over each frequency bin
        real = 0
        imag = 0
        for n in range(N):  # Loop over each time sample
            angle = 2 * math.pi * k * n / N
            real = real + x[n].real * math.cos(angle) + x[n].imag * math.sin(angle)
            imag = imag - x[n].real * math.sin(angle) + x[n].imag * math.cos(angle)
        X[k] = complex(real, imag)
    return X


def idft(X):
    """
    Compute the Inverse Discrete Fourier Transform (IDFT)

    Parameter X : List of DFT coefficients (frequency-domain representation).
    Returns   x : The reconstructed sequence in the time-domain.
    """
    N = len(X)
    x = [complex()] * N
    for n in range(N):
        real = 0
        imag = 0
        for k in range(N):
            angle = 2 * math.pi * k * n / N
            real = real + X[k].real * math.cos(angle) - X[k].imag * math.sin(angle)
            imag = imag + X[k].imag * math.cos(angle) + X[k].real * math.sin(angle)
        real = real / N  # divide by N to ensure the proper scaling
        imag = imag / N
        x[n] = complex(real, imag)
    return x

if __name__ == '__main__':
    pass

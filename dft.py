#!/usr/bin/env python
"""
Discrete Fourier Transform DFT
"""
import math


def dft(x):
    """
    Compute the Discrete Fourier Transform (DFT)

    Parameter x : List of complex numbers.
                  The time-domain signal is in the real part.
                  The imag part is not used (should be zero).
    Returns   X : List of DFT coefficients (frequency-domain representation).
    """
    N = len(x)
    X = [complex()] * N
    for k in range(N):  # Loop over each frequency bin
        real = 0
        imag = 0
        for n in range(N):  # Loop over each time sample
            angle = 2 * math.pi * k * n / N
            real +=  x[n].real * math.cos(angle) + x[n].imag * math.sin(angle)
            imag += -x[n].real * math.sin(angle) + x[n].imag * math.cos(angle)
        X[k] = complex(real, imag)
    return X


def idft(X):
    """
    Compute the Inverse Discrete Fourier Transform (IDFT)

    Parameter X : The input sequence in the frequency domain (DFT coefficients).
    Returns   x : The reconstructed sequence in the time domain.
    """
    N = len(X)
    x = [complex()] * N
    for n in range(N):
        real = 0
        imag = 0
        for k in range(N):
            angle = 2 * math.pi * k * n / N
            real += X[k].real * math.cos(angle) - X[k].imag * math.sin(angle)
            imag += X[k].imag * math.cos(angle) + X[k].real * math.sin(angle)
        x[n] = complex(real / N, imag / N)  # Normalize by N
    return x

if __name__ == '__main__':
    pass

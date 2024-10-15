#!/usr/bin/env python
"""
Discrete Fourier Transform DFT
"""
import math


def dft(x):
    """
    Compute the Discrete Fourier Transform (DFT)

    Parameter x : The input array containing time-domain signal samples.
    Returns   X : The DFT coefficients (frequency-domain representation).

    This function does not use the complex numbers type in Python.
    Format of list x and X: [(real, imag), (real, imag), ...]
    The time-domain signal is in the real part, the imag part is not used.
    """
    N = len(x)
    X = [(0, 0)] * N
    for k in range(N):  # Loop over each frequency bin
        real = 0.0
        imag = 0.0
        for n in range(N):  # Loop over each time sample
            angle = 2 * math.pi * k * n / N
            real += x[n][0] * math.cos(angle)  # mul with real part of x[n]
            imag -= x[n][0] * math.sin(angle)
        X[k] = (real, imag)
    return X


def idft(X):
    """
    Compute the Inverse Discrete Fourier Transform (iDFT)

    Parameter X : The input sequence in the frequency domain (DFT coefficients).
    Returns   x : The reconstructed sequence in the time domain.

    This function does not use the complex numbers type in Python.
    Format of list X and x: [(real, imag), (real, imag), ...]
    """
    N = len(X)
    x = [(0, 0)] * N
    for n in range(N):
        real = 0.0
        imag = 0.0
        for k in range(N):
            angle = 2 * math.pi * k * n / N
            real += X[k][0] * math.cos(angle) - X[k][1] * math.sin(angle)
            #imag += X[k][1] * math.cos(angle) + X[k][0] * math.sin(angle)
        x[n] = (real / N, imag / N)  # Normalize by N
    return x


#####################################################################
# TEST
#####################################################################

def test_show_array(array, show_magnitude=False):
    """
    Show the array with the DFT coefficients
    """
    print(' nr       real         imag         magnitude       phase')
    n = len(array)  # nur für Berechnung magnitude
    for i, (real, imag) in enumerate(array):
        print(f'{i:4} {real:12.6f} {imag:12.6f}j', end='')
        if show_magnitude:
            magnitude = 2.0/n*math.sqrt(real*real+imag*imag)
            phase = math.atan2(imag, real)
            print(f' -> {magnitude:12.6f} {phase:12.6f}', end='')
        print('')


def test_dft(samples):
    """
    Test Time-domain -> DFT -> iDFT
    """
    print('Time-domain signal:')
    test_show_array(samples)
    print("DFT:")
    X = dft(samples)  # Fourier Transformation
    test_show_array(X, True)
    print("iDFT:")
    x = idft(X)
    test_show_array(x)


def test1():
    """
    Test Simple sawtooth
    """
    print('*'*20, 'Test 1', '*'*20)
    samples = [(1, 0), (2, 0), (3, 0), (4, 0)]
    test_dft(samples)


def test2():
    """
    Test Multiple sine curves
    DC component:              150
    Amplitude fundamental:    1000
    Amplitude 2nd harmonic:    300
    """
    print('*'*20, 'Test 2', '*'*20)
    N = 16
    samples = []
    for x in range(N):
        arc = (x * 2 * math.pi) / N
        real = 150+(1000*math.sin(arc))+(300*math.sin(3*arc))
        imag = 0.0
        samples.append((real, imag))
    test_dft(samples)


if __name__ == "__main__":
    test1()
    #test2()

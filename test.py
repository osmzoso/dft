#!/usr/bin/env python
"""
Test Discrete Fourier Transform DFT
"""
import cmath
import numpy as np
import dft


def test_sample(samples):
    """
    Test the DFT functions in dft.py
    """
    error = False
    print('\n' + '*' * 30 + ' Test ' + '*' * 30)
    print('Samples:', len(samples), '\n', samples)
    # Reference DFT with numpy
    X_ref = np.fft.fft(np.array(samples))
    # Transform samples to complex numbers
    x = [complex(real) for real in samples]
    #
    print('DFT:')
    X = dft.dft(x)
    # X = dft.dft_exp(x)
    N = len(X)
    for i in range(N):
        print(f'{i:4} {X[i].real:18.8f} {X[i].imag:18.8f}j ', end='')
        if cmath.isclose(X[i], X_ref[i], abs_tol=1e-10):
            print('\033[32m' + 'OK' + '\033[0m', end='')
            magnitude = abs(X[i]) * 2 / N
            phase = cmath.phase(X[i])
            # magnitude = 2.0/n*math.sqrt(z.real*z.real+z.imag*z.imag)
            # phase = math.atan2(z.imag, z.real)
            print(f' {magnitude:12.6f} {phase:12.6f}')
        else:
            error = True
            print('\033[31m' + 'ERROR' + '\033[0m' +
                 f' X_ref: {X_ref[i].real:.18f} {X_ref[i].imag:.18f}' +
                 f' X: {X[i].real:.18f} {X[i].imag:.18f}')
    #
    print('IDFT:')
    x_inv = dft.idft(X)
    # x_inv = dft.idft_exp(X)
    N = len(x_inv)
    for i in range(N):
        print(f'{i:4} {x_inv[i].real:18.8f} {x_inv[i].imag:18.8f}j ', end='')
        if cmath.isclose(x_inv[i], x[i], abs_tol=1e-14):
            print('\033[32m' + 'OK' + '\033[0m')
        else:
            error = True
            print('\033[31m' + 'ERROR' + '\033[0m' +
                 f' x: {x[i].real:.18f} {x[i].imag:.18f}' +
                 f' x_inv: {x_inv[i].real:.18f} {x_inv[i].imag:.18f}')
    #
    return error


if __name__ == '__main__':
    test_sample([1, 2, 3, 4])
    test_sample([1+2j, 2, 3, 4])
    test_sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    test_sample([0, 1, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1, -1])
    test_sample([150, 810, 1069, 959, 850, 959, 1069, 810, 150, -510, -769, -659, -550, -659, -769, -510])

#!/usr/bin/env python
"""
Compare time requirements
"""
import time
import numpy as np
import dft


def compare_time(x):
    """
    Compare time requirements of different methods
    """
    print('Length time-domain signal:', len(x))
    n = 1

    start = time.time()
    for i in range(n):
        X = dft.dft(x)
    time_dft = time.time() - start
    print(f'Time {n} * dft()       :', time_dft)

    start = time.time()
    for i in range(n):
        X = dft.dft_exp(x)
    time_dft_exp = time.time() - start
    print(f'Time {n} * dft_exp()   :', time_dft_exp)

    start = time.time()
    for i in range(n):
        X = np.fft.fft(x)
    time_numpy_fft = time.time() - start
    factor = round(time_dft / time_numpy_fft)
    print(f'Time {n} * numpy fft() : {time_numpy_fft}'
          f' -> {factor} times faster than dft()')


def test_time_domain_signals():
    """
    Generates time-domain signals with different length
    """
    l = [8, 16, 32, 64, 128, 256, 512, 1024, 2047, 2048, 2049]
    for n in l:
        x = []
        for z in range(1, n + 1):
            x.append(z)
        compare_time(x)


if __name__ == '__main__':
    test_time_domain_signals()

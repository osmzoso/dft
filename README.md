# DFT


## Discrete Fourier Transform (DFT)

The **DFT** converts a sequence of $N$ time-domain samples into the frequency domain.  
The formula for the DFT of a signal $x[n]$, where $n = 0, 1, 2, \dots, N-1$, is:

```math
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i \cdot 2\pi \cdot k \cdot n / N}
```

Where:
- $X[k]$ is the DFT coefficient for the $k$-th frequency bin.
- $x[n]$ is the time-domain sample at index $n$.
- $N$ is the total number of samples.
- $k$ is the frequency index (from 0 to $N-1$).
- $i$ is the imaginary unit.
- The exponential $e^{-i \cdot 2\pi \cdot k \cdot n / N}$ can be expanded using Euler's formula into real and imaginary components:
```math
e^{-i \cdot 2\pi \cdot k \cdot n / N} = \cos\left( \frac{2\pi k n}{N} \right) - i \cdot \sin\left( \frac{2\pi k n}{N} \right)
```

Python Code:

```python
def dft(x):
    """
    Compute the Discrete Fourier Transform (DFT) of a 1D array x.

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
```

<https://en.wikipedia.org/wiki/Euler%27s_formula>  
<https://de.wikipedia.org/wiki/Eulersche_Formel>  


## Inverse Discrete Fourier Transform (IDFT)

Reconstruct a discrete time-domain sequence from its frequency-domain representation.

The formula for the IDFT is:

```math
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{i \frac{2\pi}{N} kn}
```
or
```math
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] \cdot \left( \cos\left(\frac{2 \pi k n}{N}\right) + i \cdot \sin\left(\frac{2 \pi k n}{N}\right)\right)
```

Where:
- $$X[k]$$ are the DFT coefficients.
- $$x[n]$$ is the result of the IDFT (the time-domain signal).
- $$N$$ is the number of samples.


The formula for IDFT in terms of real and imaginary parts is:

```math
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} \left( X_{re}[k] \cdot \cos\left(\frac{2 \pi k n}{N}\right) - X_{im}[k] \cdot \sin\left(\frac{2 \pi k n}{N}\right) \right) + i \cdot \left( X_{im}[k] \cdot \cos\left(\frac{2 \pi k n}{N}\right) + X_{re}[k] \cdot \sin\left(\frac{2 \pi k n}{N}\right) \right)
```

Where $$X_{re}[k]$$ and $$X_{im}[k]$$ are the real and imaginary parts of $$X[k]$$, respectively.

Python Code:

```python
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
```

## Links

<https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions>


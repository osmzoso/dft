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

Euler's formula:
```math
e^{-i \cdot 2\pi \cdot k \cdot n / N} = \cos\left( \frac{2\pi k n}{N} \right) - i \cdot \sin\left( \frac{2\pi k n}{N} \right)
```
Thus the exponential $e^{-i \cdot 2\pi \cdot k \cdot n / N}$ can be expanded using Euler's formula into real and imaginary components:
```math
X(k) = \sum_{n=0}^{N-1} x(n) \cdot \left[\cos\left(\frac{2\pi k n}{N}\right) - i\sin\left(\frac{2\pi k n}{N}\right)\right]
```
The formula in terms of real and imaginary parts of the signal is:
```math
X(k) = \left[ \sum_{n=0}^{N-1} \left( x_r(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right) \right] + i \cdot \left[ \sum_{n=0}^{N-1} \left( -x_r(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) \right) \right]
```

Python Code:

```python
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
```

<https://en.wikipedia.org/wiki/Euler%27s_formula>  
<https://de.wikipedia.org/wiki/Eulersche_Formel>  


## Inverse Discrete Fourier Transform (IDFT)

Reconstruct a discrete time-domain sequence from its frequency-domain representation.

The formula for the IDFT is:

```math
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] \cdot e^{i \frac{2\pi k n}{N}}
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
```

## Links

<https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions>
<https://stackoverflow.com/questions/5595425/how-to-compare-floats-for-almost-equality-in-python>  
<https://www.geeksforgeeks.org/discrete-fourier-transform-and-its-inverse-using-c>

## Complex DFT (TODO)


The Discrete Fourier Transform (DFT) of a complex time-domain signal can be expressed in terms of its real and imaginary parts by breaking down both the signal and the complex exponential.

### Formula for the DFT:

Given a signal $x(n) = x_r(n) + i \cdot x_i(n)$, where:
- $x_r(n)$ is the real part of the signal.
- $x_i(n)$ is the imaginary part of the signal.
- $i$ is the imaginary unit $\sqrt{-1}$.

The DFT of $x(n)$ for the frequency bin $k$ is given by:

```math
X(k) = \sum_{n=0}^{N-1} x(n) \cdot e^{-i \cdot \frac{2\pi k n}{N}}
```

### Breaking Down the Exponential Term

The complex exponential $e^{-i \cdot \frac{2\pi k n}{N}}$ can be rewritten using Euler's formula:

```math
e^{-i \cdot \frac{2\pi k n}{N}} = \cos\left(\frac{2\pi k n}{N}\right) - i \cdot \sin\left(\frac{2\pi k n}{N}\right)
```

### Expanding Real and Imaginary Parts

Substituting the real and imaginary parts of $x(n)$ into the DFT formula:

```math
X(k) = \sum_{n=0}^{N-1} \left[ x_r(n) + i \cdot x_i(n) \right] \cdot \left[ \cos\left( \frac{2\pi k n}{N} \right) - i \cdot \sin\left( \frac{2\pi k n}{N} \right) \right]
```

Now, expanding this:

```math
X(k) = \sum_{n=0}^{N-1} \left[ x_r(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) - x_r(n) \cdot i \cdot \sin\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot i \cdot \cos\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right]
```

### Grouping Real and Imaginary Terms

The real part of $X(k)$:

```math
\text{Re}(X(k)) = \sum_{n=0}^{N-1} \left[ x_r(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right]
```

The imaginary part of $X(k)$:

```math
\text{Im}(X(k)) = \sum_{n=0}^{N-1} \left[ -x_r(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) \right]
```

### Final Formula

Thus, the DFT in terms of real and imaginary parts of the signal is:

```math
X(k) = \left[ \sum_{n=0}^{N-1} \left( x_r(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right) \right] + i \cdot \left[ \sum_{n=0}^{N-1} \left( -x_r(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) \right) \right]
```

This formula explicitly separates the real and imaginary parts of the DFT, and can now be implemented in code as shown earlier.

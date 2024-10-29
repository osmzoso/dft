# DFT

## Discrete Fourier Transform (DFT)

The **Discrete Fourier Transform (DFT)** is a mathematical technique used to
convert a sequence of values (usually in the time domain) into a sequence of
complex numbers (representing the frequency domain). Essentially, it helps to
decompose a signal into its constituent frequencies, showing how much of
each frequency is present in the original signal.

### Formula

For a sequence $x[n]$ of $N$ samples, the DFT is given by:

```math
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i \cdot 2 \pi \cdot k \cdot n / N}, \quad \text{for } k = 0, 1, 2, \dots, N-1
```

Where:
- $X[k]$ is the DFT result at frequency index $k$,
- $x[n]$ is the input signal at sample $n$,
- $N$ is the total number of samples,
- $i$ is the imaginary unit ($i = \sqrt{-1}$),
- $e^{-i \cdot 2\pi \cdot k \cdot n / N}$ is the complex exponential (Euler's formula), representing a complex sinusoid.

When the input sequence $x[n]$ is complex, it can be represented as $x[n] = x_{\text{real}}[n] + i \cdot x_{\text{imag}}[n]$.

To express the DFT formula in terms of real and imaginary parts, we can expand the complex exponential $e^{-i \cdot 2\pi \cdot k \cdot n / N}$ using Euler's formula:

```math
e^{-i \cdot 2\pi \cdot k \cdot n / N} = \cos \left( \frac{2\pi k n}{N} \right) - i \cdot \sin \left( \frac{2\pi k n}{N} \right)
```

Substituting $x[n] = x_{\text{real}}[n] + i \cdot x_{\text{imag}}[n]$ and expanding the exponential $e^{-i \cdot 2\pi \cdot k \cdot n / N}$ using Euler's formula, we have:

```math
X[k] = \sum_{n=0}^{N-1} \left( x_{\text{real}}[n] + i \cdot x_{\text{imag}}[n] \right) \cdot \left( \cos \left( \frac{2\pi k n}{N} \right) - i \cdot \sin \left( \frac{2\pi k n}{N} \right) \right)
```

Expanding this product and grouping real and imaginary terms, we get:

```math
X[k] = \sum_{n=0}^{N-1} \left( x_{\text{real}}[n] \cdot \cos \left( \frac{2\pi k n}{N} \right) + x_{\text{imag}}[n] \cdot \sin \left( \frac{2\pi k n}{N} \right) \right) - i \sum_{n=0}^{N-1} \left( x_{\text{real}}[n] \cdot \sin \left( \frac{2\pi k n}{N} \right) - x_{\text{imag}}[n] \cdot \cos \left( \frac{2\pi k n}{N} \right) \right)
```

So the DFT of a complex sequence $x[n]$ has the following real and imaginary parts:

```math
X_{\text{real}}[k] = \sum_{n=0}^{N-1} \left( x_{\text{real}}[n] \cdot \cos \left( \frac{2\pi k n}{N} \right) + x_{\text{imag}}[n] \cdot \sin \left( \frac{2\pi k n}{N} \right) \right)
```

```math
X_{\text{imag}}[k] = \sum_{n=0}^{N-1} \left( - x_{\text{real}}[n] \cdot \sin \left( \frac{2\pi k n}{N} \right) + x_{\text{imag}}[n] \cdot \cos \left( \frac{2\pi k n}{N} \right) \right)
```

This formulas explicitly separates the real and imaginary parts of the DFT and can now be implemented in Python code:

```python
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
```



---
OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD
---

# DFT


## Discrete Fourier Transform (DFT)

The **Discrete Fourier Transform (DFT)** is a mathematical technique used to
convert a sequence of values (usually in the time domain) into a sequence of
complex numbers (representing the frequency domain). Essentially, it helps to
decompose a signal into its constituent frequencies, showing how much of each
frequency is present in the original signal.

### Formula:

The DFT of $x(n)$ for the frequency bin $k$ is given by:

```math
X(k) = \sum_{n=0}^{N-1} x(n) \cdot e^{-i \cdot \frac{2\pi k n}{N}}
```

Where:
- $X(k)$ is the DFT coefficient for the $k$-th frequency bin.
- $x(n)$ is the time-domain sample at index $n$.
  - where $x(n) = x_r(n) + i \cdot x_i(n)$
  - $x_r(n)$ is the real part of the signal.
  - $x_i(n)$ is the imaginary part of the signal (usually 0).
- $N$ is the total number of samples.
- $k$ is the frequency index (from 0 to $N-1$).
- $i$ is the imaginary unit $\sqrt{-1}$.

The complex exponential $e^{-i \cdot \frac{2\pi k n}{N}}$ can be rewritten using Euler's formula:

```math
e^{-i \cdot \frac{2\pi k n}{N}} = \cos\left(\frac{2\pi k n}{N}\right) - i \cdot \sin\left(\frac{2\pi k n}{N}\right)
```

Substituting the real and imaginary parts of $x(n)$ into the DFT formula:

```math
X(k) = \sum_{n=0}^{N-1} \left[ x_r(n) + i \cdot x_i(n) \right] \cdot \left[ \cos\left( \frac{2\pi k n}{N} \right) - i \cdot \sin\left( \frac{2\pi k n}{N} \right) \right]
```

Now, expanding this:

```math
X(k) = \sum_{n=0}^{N-1} \left[ x_r(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) - x_r(n) \cdot i \cdot \sin\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot i \cdot \cos\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right]
```

Thus, the DFT in terms of real and imaginary parts of the signal is:

```math
X(k) = \left[ \sum_{n=0}^{N-1} \left( x_r(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right) \right] + i \cdot \left[ \sum_{n=0}^{N-1} \left( -x_r(n) \cdot \sin\left( \frac{2\pi k n}{N} \right) + x_i(n) \cdot \cos\left( \frac{2\pi k n}{N} \right) \right) \right]
```

This formula explicitly separates the real and imaginary parts of the DFT, and can now be implemented in code.

Python Code:

```python
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
```


## Inverse Discrete Fourier Transform (IDFT)

The Inverse Discrete Fourier Transform (IDFT) is used to transform a frequency-domain signal back into its time-domain representation. Like the DFT, the IDFT can also be expressed in terms of its real and imaginary components.

### Formula:

The general formula for the IDFT is:

```math
x(n) = \frac{1}{N} \sum_{k=0}^{N-1} X(k) \cdot e^{i \cdot \frac{2\pi k n}{N}}
```

We can rewrite the complex exponential $e^{i \cdot \frac{2\pi k n}{N}}$ using Euler's identity:

```math
e^{i \cdot \frac{2\pi k n}{N}} = \cos\left( \frac{2\pi k n}{N} \right) + i \cdot \sin\left( \frac{2\pi k n}{N} \right)
```

Given the frequency-domain signal $X(k) = X_r(k) + i \cdot X_i(k)$, where:
- $X_r(k)$ is the real part of the frequency-domain signal.
- $X_i(k)$ is the imaginary part of the frequency-domain signal.

Substitute the real and imaginary parts of $X(k)$ into the IDFT formula:

```math
x(n) = \frac{1}{N} \sum_{k=0}^{N-1} \left[ X_r(k) + i \cdot X_i(k) \right] \cdot \left[ \cos\left( \frac{2\pi k n}{N} \right) + i \cdot \sin\left( \frac{2\pi k n}{N} \right) \right]
```

Now, expanding this:

```math
x(n) = \frac{1}{N} \sum_{k=0}^{N-1} \left[ X_r(k) \cdot \cos\left( \frac{2\pi k n}{N} \right) - X_i(k) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right] + i \cdot \left[ X_r(k) \cdot \sin\left( \frac{2\pi k n}{N} \right) + X_i(k) \cdot \cos\left( \frac{2\pi k n}{N} \right) \right]
```

Thus, the IDFT formula in terms of real and imaginary parts is:

```math
x_r(n) = \frac{1}{N} \sum_{k=0}^{N-1} \left( X_r(k) \cdot \cos\left( \frac{2\pi k n}{N} \right) - X_i(k) \cdot \sin\left( \frac{2\pi k n}{N} \right) \right)
```

```math
x_i(n) = \frac{1}{N} \sum_{k=0}^{N-1} \left( X_r(k) \cdot \sin\left( \frac{2\pi k n}{N} \right) + X_i(k) \cdot \cos\left( \frac{2\pi k n}{N} \right) \right)
```

Python Code:

```python
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
```


## Links

<https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions>
<https://stackoverflow.com/questions/5595425/how-to-compare-floats-for-almost-equality-in-python>  
<https://www.geeksforgeeks.org/discrete-fourier-transform-and-its-inverse-using-c>

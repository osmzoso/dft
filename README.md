# dft
Discrete Fourier Transform

To avoid using complex multiplication and instead break it down into real and imaginary parts, we can separate the real and imaginary components of the input signal, perform the necessary operations, and then combine the results. This avoids directly multiplying complex numbers.

The formula for **IDFT** in terms of real and imaginary parts is:

$$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} \left( X_{re}[k] \cdot \cos\left(\frac{2 \pi k n}{N}\right) - X_{im}[k] \cdot \sin\left(\frac{2 \pi k n}{N}\right) \right) + i \cdot \left( X_{im}[k] \cdot \cos\left(\frac{2 \pi k n}{N}\right) + X_{re}[k] \cdot \sin\left(\frac{2 \pi k n}{N}\right) \right)$$

Where:
- \( X_{re}[k] \) and \( X_{im}[k] \) are the real and imaginary parts of \( X[k] \), respectively.

Here’s the Python code that separates the real and imaginary parts explicitly and avoids complex multiplication:

```python
import numpy as np

def idft_real_imag(X):
    """
    Compute the Inverse Discrete Fourier Transform (IDFT) of a sequence X
    by separating real and imaginary parts, avoiding complex multiplication.
    
    Parameters:
    X : array-like
        The input sequence in the frequency domain (DFT coefficients).
    
    Returns:
    x : np.array
        The reconstructed sequence in the time domain.
    """
    N = len(X)
    x_real = np.zeros(N)
    x_imag = np.zeros(N)
    
    # Separate real and imaginary parts of X[k]
    X_re = X.real
    X_im = X.imag
    
    for n in range(N):
        sum_real = 0
        sum_imag = 0
        for k in range(N):
            angle = 2 * np.pi * k * n / N
            cos_term = np.cos(angle)
            sin_term = np.sin(angle)
            
            # Real part contribution
            sum_real += X_re[k] * cos_term - X_im[k] * sin_term
            # Imaginary part contribution
            sum_imag += X_im[k] * cos_term + X_re[k] * sin_term
        
        # Normalize by N
        x_real[n] = sum_real / N
        x_imag[n] = sum_imag / N
    
    # Combine real and imaginary parts into a complex result
    x = x_real + 1j * x_imag
    return x

# Example usage:
# X is the frequency domain representation (DFT coefficients)
X = np.array([1, 2, 3, 4], dtype=complex)
# Compute IDFT
x = idft_real_imag(X)
print("IDFT Result:", x)
```

### Explanation:
- The input `X` is separated into its real (`X_re`) and imaginary (`X_im`) components.
- For each time index `n`, we loop over all frequency components `k` and compute the real and imaginary contributions separately:
  - **Real part**: Calculated as \( X_{re}[k] \cdot \cos(\theta) - X_{im}[k] \cdot \sin(\theta) \).
  - **Imaginary part**: Calculated as \( X_{im}[k] \cdot \cos(\theta) + X_{re}[k] \cdot \sin(\theta) \).
- The two sums (real and imaginary) are accumulated separately and normalized by `N`.
- Finally, the real and imaginary results are combined into a complex array `x`.

This code now avoids complex multiplication by explicitly handling the real and imaginary components.

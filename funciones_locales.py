# funciones_locales.py
import numpy as np 
from math import factorial as fact
from scipy.special import gamma


# Funciones de distribuciones de probabilidad discretas 
 
def combinatorial(n, k):
    if k < 0 or k > n:
        return 0
    else:
        return fact(n) / (fact(k) * fact(n - k))



# definicion de la funcion binomial
def bin(x, n, p):
    return combinatorial(n, x) * p**x * (1-p)**(n-x)

# binomial negativa
def bin_neg(x, r, p):
    return combinatorial(x+r-1, r-1) * p**r * (1-p)**x

# definicion de la funcion de Poisson
def poisson(x, l):
    return (l**x * np.exp(-l)) / fact(x)

# Hipergeometrica 
def hipergeom(x, n, M, N):
    return combinatorial(M, x) * combinatorial(N-M, n-x) / combinatorial(N, n)



# Funciones de distribuciones de probabilidad continuas

# Para la distribucion normal
def N(x, mu, sigma):
    return (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

# Distribución chi-cuadrado
def chi2(x, k):
    if x < 0:
        error = "Error: x debe ser mayor o igual a 0"
        raise ValueError(error)
    else:
        num = (0.5)**(k/2) * x**(k/2 - 1) * np.exp(-x/2)
        f = num / gamma(k/2)

    return f

# Distribucion de Weibull
def weibull(x, alpha, beta):
    if np.any(x < 0):
        error = "Error: x debe ser mayor o igual a 0"
        raise ValueError(error)
    else:
        if beta <= 0:
            error = "Error: alpha y beta deben ser mayores a 0"
            raise ValueError(error)
        return (alpha/ beta) * (x / beta) ** (alpha - 1) * np.exp(-(x / beta) ** alpha)




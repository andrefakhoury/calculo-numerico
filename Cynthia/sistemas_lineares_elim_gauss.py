# -*- coding: utf-8 -*-
"""sistemas_lineares_elim_gauss.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z_lgTvW9NAa6fJXMWpcFb76fZdp-qOWv
"""

import numpy as np

# Eliminação de Gauss
# x = gaussElimin(a,b).
# Solves [a]{b} = {x} by Gauss elimination.


def gaussElimin(a,b):
 n = len(b)
 # Elimination phase
 for k in range(0,n-1):
   for i in range(k+1,n):
     if a[i,k] != 0.0:
        lam = a [i,k]/a[k,k]
        a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
        b[i] = b[i] - lam*b[k] 
 # Back substitution
 for k in range(n-1,-1,-1):
    b[k] = (b[k] - a[k,k+1:n].dot(b[k+1:n]))/a[k,k]
 return b

  # Exemplo 
A = np.array([[1, 2,0], [1, 3,1],[-2, 0,1]])
b = np.array([3,5,-1])
x = gaussElimin(A,b)
print(x)

"""Considere o sistema

2x-y=1

-x+2y-z=0

-y+z=0

Vamos aplicar o método da eliminação de gauss a este sistema. O que aconteceu ?
"""

A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 1]])
b = np.array([1,0,0])
x = gaussElimin(A,b)
print(x)
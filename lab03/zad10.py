import math

from lab03.zad8 import odlegloscM2Pkt


def czy_wspolliniowe(A, B, C):
    pole = abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[0])) / 2
    return pole == 0

def obwodTrojkata(A, B, C):
    if czy_wspolliniowe(A, B, C):
        print("Punkty są wspóliniowe - nie jest to trójkąt")
        return 0
    return odlegloscM2Pkt(A, B) + odlegloscM2Pkt(B, C) + odlegloscM2Pkt(C, A)

A = [0, 0]
B = [1, 1]
C = [2, 2]
print(obwodTrojkata(A, B, C))
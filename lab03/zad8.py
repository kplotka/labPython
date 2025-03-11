import math

def odlegloscM2Pkt(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def obwodTrojkata(A, B, C):
    return odlegloscM2Pkt(A, B) + odlegloscM2Pkt(B, C) + odlegloscM2Pkt(C, A)

A = [0, 0]
B = [3, 0]
C = [0, 4]
print(obwodTrojkata(A, B, C))
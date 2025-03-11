import math

def odlegloscM2Pkt(A, B):
    return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

A = [6, 1]
B = [2, 4]
print(odlegloscM2Pkt(A, B))
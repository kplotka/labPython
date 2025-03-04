from itertools import permutations

def unique_permutations(elements: list):
    return list(set(permutations(elements)))

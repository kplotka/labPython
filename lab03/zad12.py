def czy_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(czy_anagram("listen", "silent"))
print(czy_anagram("kot", "tok"))
print(czy_anagram("python", "java"))
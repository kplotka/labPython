def longest_increasing_subsequence(sequence: list[int]) -> int:
    maxlen = 0
    currentlen = 1

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            currentlen += 1
        else:
            maxlen = max(maxlen, currentlen)
            currentlen = 1

    return max(maxlen, currentlen)
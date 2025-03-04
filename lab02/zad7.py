from collections import Counter

def most_frequent_element(data: list):
    return Counter(data).most_common(1)[0][0]
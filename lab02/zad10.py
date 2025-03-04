from collections import defaultdict

def group_words_by_length(words: list[str]) -> dict:
    grouped = defaultdict(list)
    for word in words:
        grouped[len(word)].append(word)
    return dict(grouped)

import re

def count_syllables(word: str) -> int:
    return max(1, len(re.findall('[aeyuio]+', word.lower())))

def readability_score(text: str) -> float:
    sentences = re.split('[.!?]', text)
    words = text.split()

    num_sentences = max(1, len([s for s in sentences if s.strip()]))
    num_words = len(words)
    num_syllables = sum(count_syllables(word) for word in words)

    avg_syllables_per_word = num_syllables / num_words
    avg_words_per_sentence = num_words / num_sentences

    #wskaznik czytelnosci Flescha
    return 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
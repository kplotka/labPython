def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text
    chars = list(text)
    for i in range(0, len(text) - key, key):
        chars[i], chars[i + key] = chars[i + key], chars[i]
    return ''.join(chars)
def szyfr_cezara(tekst, przesuniecie):
    zaszyfrowany = ""
    for znak in tekst:
        if znak.isalpha():
            kod = ord(znak) + przesuniecie
            if znak.islower():
                zaszyfrowany += chr((kod - ord('a')) % 26 + ord('a'))
            else:
                zaszyfrowany += chr((kod - ord('A')) % 26 + ord('A'))
        else:
            zaszyfrowany += znak
    return zaszyfrowany

print(szyfr_cezara("Python", 3)) 

def caesar_encrypt(text, ind):
    b = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            b += chr((ord(char) - base + ind) % 26 + base)
        else:
            b += char
    return b
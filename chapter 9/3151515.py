def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char!=' ':
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Ввод данных
text = 'Osincev is a faggot'
shift = 15
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)

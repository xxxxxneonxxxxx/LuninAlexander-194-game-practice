def caesar_bruteforce(x):
    for y in range(26):
        z = ""
        for w in x:
            if w.isalpha():
                v = 65 if w.isupper() else 97
                z += chr((ord(w) - v - y) % 26 + v)
            else:
                z += w
        print(f"{y}: {z}")
x = ""
caesar_bruteforce(x)

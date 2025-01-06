def x(key):
    m = {}
    n = len(key)
    if n % 2 != 0:
        raise ValueError("Длина ключа должна быть четной.")
    for i in range(0, n, 2):
        a = key[i]
        b = key[i + 1]
        m[a] = b
        m[b] = a
        m[a.upper()] = b.upper()
        m[b.upper()] = a.upper()
    return m

def encode(msg, key):
    z = x(key)
    return "".join(z.get(c, c) for c in msg)

def decode(enc_msg, key):
    return encode(enc_msg, key)

# Примеры использования
print(encode("ABCD", "gaderypoluki"))
print(encode("Ala has a cat", "gaderypoluki"))
print(decode("Dkucr pu yhr ykbir", "politykarenu"))
print(decode("Hmdr nge brres", "regulaminowy"))

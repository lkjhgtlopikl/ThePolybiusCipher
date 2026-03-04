import random
key = random.randbytes(64)
keys_for_round = []
for i in range(0, len(key), 4):
    keys_for_round.append(key[i:i + 4])
sBox = [random.sample(range(4), 4) for _ in range(16)]
sBox = [{i: s[i] for i in range(len(s))} for s in sBox]
text = input("Введите текст: ")
coded = bytes()
text = text.encode("utf-8")
print(f"\t  Исходные байты: {text}")
for i in range(0, len(text), 8):
    block = text[i:i + 8]
    if len(block) < 8:
        block = block + b'\x00' * (8 - len(block))
    L, R = block[0:4], block[4:8]
    for j in range(16):
        L_int = int.from_bytes(L, byteorder='big')
        key_int = int.from_bytes(keys_for_round[j], byteorder='big')
        L_int = L_int ^ key_int

        L = L_int.to_bytes(4, byteorder='big')
        L = list(L)
        temp_L = L.copy()
        for k,l in sBox[j].items():
            temp_L[k] = L[l]
        L = temp_L
        L = bytes(L)

        L_int = int.from_bytes(L, byteorder='big')
        R_int = int.from_bytes(R, byteorder='big')
        L_int = L_int ^ R_int
        L = L_int.to_bytes(4, byteorder='big')
        R = R_int.to_bytes(4, byteorder='big')
        if j < 15:
            L, R = R, L
    coded += (L) + (R)
print(f"Зашифрованные данные: {coded}")
sBox_revers = [{i: j for j, i in s.items()} for s in sBox]
decoded = bytes()
for i in range(0, len(coded), 8):
    block = coded[i:i + 8]
    L, R = block[0:4], block[4:8]
    for j in range(15, -1, -1):
        if j < 15:
            L, R = R, L

        R_int = int.from_bytes(R, byteorder='big')
        L_int = int.from_bytes(L, byteorder='big')
        L_int = L_int ^ R_int
        L = L_int.to_bytes(4, byteorder='big')

        L = list(L)
        temp_L = L.copy()
        for k, l in sBox_revers[j].items():
            temp_L[k] = L[l]
        L = temp_L
        L = bytes(L)

        L_int = int.from_bytes(L, byteorder='big')
        key_int = int.from_bytes(keys_for_round[j], byteorder='big')
        L_int = L_int ^ key_int
        L = L_int.to_bytes(4, byteorder='big')

    decoded += L + R
decoded = decoded.rstrip(b'\x00')
print(f"Расшифровано (байты): {decoded}")
print(f"Расшифровано (данные): {decoded.decode("utf-8", errors='ignore')}")
print(decoded == text)

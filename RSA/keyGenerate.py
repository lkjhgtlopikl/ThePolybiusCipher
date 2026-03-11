import math
import random


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def egcd(a, b):
    # расширенный алгоритм Эвклида для поиска мультипликативно обратного числа
    x1, x2, y1, y2 = 1, 0, 0, 1
    while b > 0:
        q = a // b
        a, b = b, a % b
        x1, x2, = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
    return y1


# Выбор 2 случайных чисел

p = random.randint(1, 1000)
q = random.randint(1, 1000)

# p = 19
# q = 41
while not (isPrime(p) and isPrime(q)):
    p = random.randint(1, 1000)
    q = random.randint(1, 1000)
N = p * q
# Функция Эйлера
f = (p - 1) * (q - 1)
e = 3
# Поиск взаимно простого числа для f
for i in range(3, f):
    if math.gcd(i, f) == 1:
        e = i
        break
y = egcd(f, e)
d = y % f
print(f"N = {N}, f = {f}, e = {e}, d = {d}")
file = open("keys.txt", "w")
file.write("Открытый ключ: \n\t e = " + str(e) + ", \n\t n = " + str(N))
file.write("\nЗакрытый ключ: \n\t d = " + str(d) + ", \n\t n = " + str(N))
file.close()
# проверка мультипликативной обратности
print((e * d) % f)
# e, n - открытый ключ
# d, n - закрытый ключ

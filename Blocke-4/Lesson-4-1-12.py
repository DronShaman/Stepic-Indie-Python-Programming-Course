# В первый день спортсмен пробежал X километров.
# В каждый последующий день он увеличивал пробег на 15% от предыдущего дня.
# Вам необходимо определить номер дня, в который пробег спортсмена составил не менее Y километров.
# Само число Y будет поступать на вход программе.

a = list(map(int, input().split()))
x = a[0]
y = a[1]
n = 1
while x <= y:
    x = x + (x * 0.15)
    n += 1
print(n)
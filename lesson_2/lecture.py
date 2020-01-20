""" математические операторы и приоритеты """
a = 1 + 2
b = 2 - 1
c = 2 * 2
d = 4 / 2

a += 2  # a = a + 2
b -= 1  # b = b - 1
c *= 2  # c = c * 2
d /= 2  # d = d / 2

fa = 2.0e-1  # 2 * 0.1
fb = 2.0e3
print(fb)

a = 2  # int
print(type(a))
b = 3  # int
f = 2 / 3  # float
print(type(f))

print(type('hello'))

integer_part = a // b
print(integer_part, type(integer_part))

integer_part = 10 // 3
print(integer_part, type(integer_part))

module = 10 % 3
# module = 10 - integer_part
# 10 = 3 + 3 + 3 + 1
print(module, type(module))

s = 2 ** 2
print(s)

s = 2 ** 3
print(s)

s = 2 ** -2  # 1 / 2^2
print(s)

s = 2 ** (1/2)  # sqrt(2)
print(s)

s = 2 ** (1/3)  # кубический корень из 2
print(s)

""" логические операции """
a = True
b = False
c = 1 == 1  # равны
d = 2 > 1  # больше
e = 1 < 2  # меньше
f = 2 >= 2
g = 1 <= 1
h = 1 != 2  # не равны
h1 = 2 in [1, 2]
h3 = 2 not in [1, 3]

# операторы объединения логических конструкций
# and, or, not
# not True == False
# not False == True
# True and True == True
# True and False == False
# True or True == True
# True or False == True

# 2 + 3 * 4 = 2 + 12
# 2 + 3 ** 2 = 2 + 9

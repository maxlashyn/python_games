""" list """

a = []  # пустой список
print(a)

b = [1, 2, 3, 4]
print(b)

""" multidimension list """
c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(c)

d = [1, 's', 2.0, 0x23, 'q']
print(d)

Max = [14, 50, 'Max']
print(Max)

""" operation with list """
Max.append('Lashyn')
print(Max)
print(Max.index('Lashyn'))
Max.remove('Lashyn')
print(Max)
Max.insert(2, 'Lashyn')
print(Max)
print(Max[3])
print(Max[1:3])
print(Max[:3])
print(Max[2:])
Max[1] = 15
print(Max)

print(c[1])
print(c[1][2])


""" list generation """

a = []
for i in range(0, 10):
    a.append(i + 2)
print(a)

a = [i + 2 for i in range(0, 10)]
print(a)

""" list-based queue """
""" FIFO """

q = [1, 2, 3, 4, 5]
q.reverse()
print(q)
for i in range(len(q)):
    print(q.pop())

q = [i for i in range(10)]
print(q)
for i in range(len(q)):
    x = q[i]
    print(x)
q.clear()

""" list-based stack """
""" LIFO """

q = [i for i in range(10)]
print(q)
for i in range(len(q)):
    print(q.pop())
print(q)

""" tuples immutable """

q = 1, 2, 3
print(q)
q = (1, 2, 3, 4)
print(q)
# выдаст ошибку q[0] = 1
q = ((1, 2, 3), 3, [1, 3, 4])
print(q)
print(q[1])

q = list([1, 2, 3])
print(q)

g, t = 1, 2
g1, t1 = (10, 20)
print(f"{g} - {t}")

g, t = t, g
print(f"{g} - {t}")

""" set """

s = {2, 3, 4, "qweqwe"}
print(s)
s = set([2, 3, 5])
print(s)
print(2 in s)
print(6 in s)

"""  dictionary """

d = {'age': 14, 'weight': 50, 'name': Max}
print(d)
print(d['age'])

d['age'] = 15
print(d)
print(d.keys())

""" for with k, v """
for key, value in d.items():
    print("%s = %s" % (key, value))
    print(f"{key} = {value}")

""" enumerate() """
for key, value in enumerate(d):  # (позиция ключа в словаре, название ключа)
    print(f"{key} = {value}")

""" zip() """

w = [10, 20, 30]
x = [4, 5, 6]
for key, value in zip(w, x):
    print(f"{key} = {value}")


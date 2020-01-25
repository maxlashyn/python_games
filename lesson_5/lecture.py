""" f = open(name, type) """

#f = open('test.txt', 'w')
# f.write('русский текст')

f = open('test.txt', 'r', encoding='cp1251')
print(f.read(2))
print(f.read(2))  # читает n символов
print(f.tell())  # позиция чтения
f.seek(5)  # переместить позицию чтения 0 - с начала, 1 - с конца, 2 - с текущей позиции
print(f.read())  # читает весь файл от текущей позиции чтения до конца
f.close()

f = open('test.txt', 'r', encoding='cp1251')
print(f.readline())  # чтение одной строки до символа перевода каретки
f.close()

f = open('test.txt', 'r', encoding='cp1251')
# выбор всех строк из файла
for line in f:
    print(line)
f.close()

f = open('test.txt', 'r', encoding='cp1251')
text = f.readlines()
print(text)
f2 = open('test2.txt', 'w')
f2.writelines(text)
f2.close()
f3 = open('test_append.txt', 'a')
f3.writelines(text)
f3.writelines(text)
f.close()

with open('test2.txt', 'r') as f:  # автоматом закрывает файл после выполнения последней команды в секции
    print(f.read())


a = list('test word')
print(a)

import json

print(json.dumps(a))  # преобразовали список в json формат
print(a)
f = open('test_json.txt', 'w')
json.dump(a, f)  # сохранили список в файл в json формате
f.close()

f = open('test_json.txt', 'r')
b = json.load(f)  # восстанавливаем (загружаем) список из файла
print(b)
f.close()

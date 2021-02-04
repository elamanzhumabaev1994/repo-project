str = input("Введите строку из нескольких слов, разделённых пробелами: ")
a = str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. {el}")
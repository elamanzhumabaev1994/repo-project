el_count = int(input("Для заполнения списка введите количество элементов: "))
elements = []
i = 0
el = 0
while i < el_count:
    elements.append(input("Введите значение: "))
    i += 1

for i in range(int(len(elements) / 2)):
    elements[el], elements[el + 1] = elements[el + 1], elements[el]
    el += 2
print(elements)

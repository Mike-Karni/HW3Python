'''Напишите программу, которая определит позицию
второго вхождения строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1 '''

list  = ['1','2','3','4','66','2','66']
print(list.count('11'))

'''
x=[["hi hello"], ["this is other"],["this"],["something"],["this"],["last element"]]
for index, line in enumerate(x):
    print(index, line)'''


'''
0 ['hi hello']
1 ['this is other']
2 ['this']
3 ['something']
4 ['this']
5 ['last element']'''
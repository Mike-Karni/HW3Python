'''Напишите программу, которая определит позицию
второго вхождения строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1 '''

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
text = 'qwe'

count = list.count('qwe')


indexFirst = list.index(text)
indexSecond = 0
for i in list:
    if text in list:
        if count == 2:
            indexSecond = list.index(text,indexFirst+1,len(list)-1)
            print(indexSecond)
            break
        else:
            print('-1')
            break
    else:
        print('-1')
        break





'''Напишите программу, которая определит позицию
второго вхождения строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1 '''



list = ["qwe", "asd", "abs", "qwe", "ertqwe"]
text = input("Введите элемент списка на проверку ")
count = list.count(text)
try :
    indexFirst = list.index(text)
except:
    print("Данный элемент не находится в списке")
indexSecond = 0
for i in list:
    if text in list:
        if count >= 2:
            indexSecond = list.index(text,indexFirst+1,len(list)-1)
            print(f"Индекс второго вхождения равен {indexSecond}")
            break
        else:
            print('-1')
            break
    else:
        print('-1')
        break


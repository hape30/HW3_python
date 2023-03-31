arr = input()
#получаем данные
if arr.count('f') == 1:
#если встречается один раз
    print(arr.find('f'))
elif arr.count('f') >= 2:
#если 2 раза и более 
    print(arr.find('f'), arr.rfind('f'))
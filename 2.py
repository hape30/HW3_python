
#первое число 
van = [0]

def morsa():
    #счётчик чисел
    count = 0
    
    while count < n:
        count += 1
        for i in range(len(van)):
            if n == len(van):
                return van
            #если 0 добавляем инверсию(0) в конец
            if van[i] == 0:
                van.append(1)
            #если 1 добавляем инверсию(0) в конец
            else:
                van.append(0)
    return van
#количество цифр в выводе
n = int(input())

print(*morsa())
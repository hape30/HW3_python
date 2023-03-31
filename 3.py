#Входные данные
van = list(map(int, input().split()))
#сначала последний элемент +  остальные элементы списка
van = [van[-1]] + van[:-1]
print(van)
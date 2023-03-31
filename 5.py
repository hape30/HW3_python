#Входные данные
van = list(map(int, input().split()))

count = 0 

for i in range(len(van)):
    for j in range(len(van)-i-1):
        #сравниваем число с последующими
        if van[i] == van[len(van)-j-1]:
            count += 1
print(count)
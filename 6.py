c=int(input())
#входные данные
a=[input().split() for i in range(c)]
#вводим массив
ans='YES'
for i in range(c):
    for j in range(i+1, c):
        #если симметричен, то стобцы = строкам (по значениям)
        if a[i][j] != a[j][i]:
            ans='NO'
print(ans)

def can_eat(a, b):
    #входные данные
    x1, y1 = a
    x2, y2 = b
    #фигура передвигается [по оси х на 2 и по оси y на 1] или [по оси х на 1 и по оси y на 2]
    if (abs(x1 - x2) == 2 and abs(y1-y2) == 1) or (abs(x1 - x2) == 1 and abs(y1-y2) == 2):
        return True
    return False



print("result = ", can_eat((2, 1), (4, 2)))

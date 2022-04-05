#!/usr/bin/python
# Filename: func_return.py
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y
print('максимум из х и у - ', maximum(2, 3))
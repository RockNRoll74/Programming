def total(initial=5, *numbers, extra_number=1):
    count = initial
    for number in numbers:
        count += number
        #Обратите внимание на использование +=, который представляет собой сокращённый оператор, 
        #позволяющий вместо x = x + y просто написать x += y.
    count += extra_number #count = count + extra_number
    print(count)
total(10, 1, 2, 3, extra_number=50)
total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.
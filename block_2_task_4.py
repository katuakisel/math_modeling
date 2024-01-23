fib1 = fib2 = 1
 
n = int(input('номер элемента ряда Фибоначчи: '))
 
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
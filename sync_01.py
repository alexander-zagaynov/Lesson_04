import time


def count_down(n):
    for i in range(n, 0, -1 ):
        print(i)
        time.sleep(1)


count_down(5)


def slow_function():
    print('Начало функции')
    time.sleep(5)
    print("конец функции")


print('Начало программы')
slow_function()
print('конец программы')









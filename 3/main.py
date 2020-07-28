from math import exp

print("Задача обратного интерполирования (1 способ)\nВариант 5\nf(x) = 1 - exp(-2x)\n")
print("Начало отрезка, a:")
a = float(input())
print("Конец отрезка, b:")
b = float(input())
print("Число значений в таблице, m+1:")
m = int(input()) - 1
r = 1


# Исходная функция
def f(y):
    return 1 - exp(-2 * y)


while r:
    print("Введите искомое значение функции, F:")
    F = float(input())

    print("Введите степень интерполяционного многочлена (n<=m),  n:")
    n = int(input())

    while n > m:
        print("Введите другое n, (n<=m),  n:")
        n = int(input())

    # Заполняем массив узлами и значениями функции в них
    values = []
    for i in range(m + 1):
        xi = (a + i * (b - a) / m)
        values.append((abs(F - f(xi)), f(xi), xi))

    values.sort()


    # Разделелённые разности
    def div_diff(a, b):
        if a > b:
            exit(0)
        if a == b:
            return values[a][2]
        else:
            return (div_diff(a + 1, b) - div_diff(a, b - 1)) / (values[b][1] - values[a][1])


    # Метод Ньютона
    def newton(z):
        ans = 0
        t = 1
        for k in range(n + 1):
            ans += div_diff(0, k) * t
            t *= (z - values[k][1])
        return ans


    # Накопленные произведения для Лагранжа
    def mult(k, z):
        t = 1
        for p in range(n + 1):
            if p != k:
                t *= (z - values[p][1])
        return t


    # Метод Лагранжа
    def lagrange(q):
        ans = 0

        for t in range(n + 1):
            ans += values[t][2] * mult(t, q) / mult(t, values[t][1])
        return ans


    # Вывод таблицы значений
    print('i)  f(x_i)  |  x_i')
    for i in range(len(values)):
        print(str(i + 1) + ')', values[i][1], '|', values[i][2])

    X = newton(F)
    print('\nМетод Ньютона, Q_n(F) = X =', X)
    print('Значение функции в этой точке, f(X)=', f(X))
    print('Модуль невязки, r_n(X) =', abs(f(X) - F))

    X = lagrange(F)
    print('\nМетод Лагранжа, Q_n(F) = X =', X)
    print('Значение функции в этой точке, f(X)=', f(X))
    print('Модуль невязки, r_n(X) =', abs(f(X) - F))

    print("Введите 0 для выхода, 1 для продолжения: ")
    r = int(input())

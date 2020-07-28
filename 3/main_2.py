from math import exp

print("Задача обратного интерполирования (2 способ)\nВариант 5 \nf(x) = 1 - exp(-2x)\n")
print("Начало отрезка, a:")
a = float(input())
print("Конец отрезка, b:")
b = float(input())
print("Число значений в таблице, m+1:")
m = int(input()) - 1
r = 1


def f(y):
    # return 1 - exp(-2 * y)
    return y ** 2


while r:

    print("Введите искомое значение функции, F:")
    F = float(input())

    print("Введите степень интерполяционного многочлена (n<=m),  n:")
    n = int(input())

    while n > m:
        print("Введите другое n, (n<=m),  n:")
        n = int(input())

    print("Введите точность, eps:")
    eps = float(input())

    values = []


    # Разделелённые разности
    def div_diff(a_, b_):
        if a_ > b_:
            exit(0)
        if a_ == b_:
            return values[a_][2]
        else:
            return (div_diff(a_ + 1, b_) - div_diff(a_, b_ - 1)) / (values[b_][1] - values[a_][1])


    # Метод Ньютона
    def newton(z):
        ans = 0
        t = 1
        for k in range(n + 1):
            ans = ans + (div_diff(0, k) * t)
            t = t * (z - values[k][1])
        return ans


    # Накопленные произведения для Лагранжа
    def mult(k, z):
        t = 1
        for p in range(n + 1):
            if p != k:
                t = t * (z - values[p][1])
        return t


    # Метод Лагранжа
    def lagrange(q):
        ans = 0
        for t in range(n + 1):
            ans = ans + (values[t][2] * mult(t, q) / mult(t, values[t][1]))
        return ans


    # Функция signum
    def sgn(x):
        if x > 0:
            return 1
        else:
            if x < 0:
                return -1
            else:
                return 0


    # Массив корней
    roots = []


    # Отделение корней
    def root_sep(a_, b_):
        h = (b_ - a_) / m
        k = 0
        x1 = a_
        x2 = x1 + h
        y1 = f(x1) - F

        while x2 <= b_:
            y2 = f(x2) - F
            if y1 * y2 < 0 or y2 == 0:
                roots.append((x1, x2))
                k = k + 1
            # print("x1", x1, "x2", x2)
            # print("y1", y1, "y2", y2)
            x1 = x2
            x2 = x1 + h
            y1 = y2
        print("Количество корней: ", k)
        return k


    # Метод бисекции
    def bisection(a_, b_):
        global values
        k = 0
        x = (a_ + b_) / 2
        if f(a_) - F == 0:
            print("Корень: ", a_)
        if f(b_) - F == 0:
            print("Корень: ", b_)

        while (b_ - a_) > eps:
            d = (b_ - a_) / 2
            x = a_ + d

            values = []
            for j in range(m + 1):
                xl = (a + j * (b - a) / m)
                values.append((abs(x - xl), xl, f(xl)))
            values.sort()

            n_x = newton(x)

            values = []
            for j in range(m + 1):
                xl = (a + j * (b - a) / m)
                values.append((abs(a_ - xl), xl, f(xl)))
            values.sort()

            a_x = newton(a_)

            if sgn(a_x - F) != sgn(n_x - F):
                b_ = x
            else:
                a_ = x
            k = k + 1
        print('\nx = ', x,
              '\nТочность:', eps,
              "\nПолучено за ", k, 'шагов',
              '\nПоследняя длина интервала:', abs(b_ - a_),
              '\nМодуль невязки: ', abs(f(x) - F))


    # Отделяем корни
    root_sep(a, b)

    print('i)  x_k  |  x_k+1')
    for i in range(len(roots)):
        print(str(i + 1) + ')', roots[i][0], '|', roots[i][1])

    for i in range(len(roots)):
        bisection(roots[i][0], roots[i][1])
    print("Введите 0 для выхода, 1 для продолжения: ")
    r = int(input())

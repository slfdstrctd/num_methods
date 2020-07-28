import math

# import numpy as np
# from sympy import Symbol, integrate, lambdify, solve, re
print("Квадратурные формулы наивысшей алгебраической степени точности (формулы типа Гаусса)\nВариант 5\n")


# Весовая функция p(x)
def p(y):
    return 1 / y ** (1 / 3)


# Функция f(x)
def f(y):
    return math.cos(y)


# Функция phi(x) = p(x)f(x)
def phi(y):
    return f(y) * p(y)


# Моменты
def m(i_, a_, b_):
    if i_ == 0:
        return 3 / 2 * (b_ ** (2 / 3) - a_ ** (2 / 3))  # m_0(x)
    if i_ == 1:
        return 3 / 5 * (b_ ** (5 / 3) - a_ ** (5 / 3))  # m_1(x)


# Накопленные произведения для Лагранжа
def mult(k, z):
    t = 1
    for p in range(m + 1):
        if p != k:
            t = t * (z - values[p])
    return t


# Метод Лагранжа
def lagrange(q):
    ans = 0
    for t in range(m + 1):
        ans = ans + (f(values[t]) * mult(t, q) / mult(t, values[t]))
    return ans


# КФ средних прямоугольников
def mid():
    s = 0
    for j in range(m):
        s = s + phi(values[j + 1] - h / 2)

    return h * s


# Формула Гаусса
def gauss():
    global values
    values = [-(0.6 ** 0.5), 0, 0.6 ** 0.5]
    p_ = [-0.4, -0.5, 0.4]
    a_ = []
    for j in range(m + 1):
        # print(j, values[j], p_[j])
        a_.append((2 * (1 - values[j] ** 2)) / (((m + 1) ** 2) * p_[j] ** 2))

    sum_ = 0
    for j in range(m + 1):
        # print(a_[j], phi((b - a) * values[j] / 2 + (b + a) / 2))
        sum_ += a_[j] * phi((b - a) * values[j] / 2 + (b + a) / 2)
    return ((b - a) / 2) * sum_


r = 1
while r:
    print("Функция phi(x) = cos(x)/x^(1/3):\np(x) = 1/x^(1/3), f(x) = cos(x)\n")
    print("Нижний предел интегрирования, A = 0")
    a = 0
    print("Верхний предел интегрирования, B = 1")
    b = 1
    print("Число промежутков деления, m:")
    m = int(input())

    values = []
    h = (b - a) / m  # длина частичного разбиения

    # Массив узлов
    for i in range(m + 1):
        xi = (a + i * h)
        values.append(xi)

    print('h =', h)

    # точный интеграл phi от 0 до 1
    j_ = 1.3212230741459003099469074212370546202293316300043820048748526319098001457707427010561826248610759312

    print('Точное значение интеграла J =', j_)
    int_ = mid()

    print('\nМетод средних прямоугольников, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))

    # print(lagrange(0))
    values = [1 / 4, 3 / 4]
    a_0 = (3 / 5 - 3 / 2 * values[1]) / (values[0] - values[1])
    a_1 = (3 / 5 - 3 / 2 * values[0]) / (values[1] - values[0])
    int_ = a_0 * f(values[0]) + a_1 * f(values[1])

    # print('\nУзлы: 1/4, 3/4')
    print('\nИнтерполяционный метод, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))

    int_ = gauss()
    print('\nФормула Гаусса, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))

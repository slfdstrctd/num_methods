import math
import numpy as np
from sympy import Symbol, integrate, lambdify, solve, re

x = Symbol('x')

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


# КФ средних прямоугольников
def mid():
    s = 0
    for j in range(m):
        x_ = values[j + 1] - h / 2
        print(x_)
        s = s + phi(x_)

    return h * s


# Формула Гаусса
def gauss():
    global values
    values = [-(0.6 ** 0.5), 0, 0.6 ** 0.5]
    p_ = [-0.4, -0.5, 0.4]
    # a_ = [5 / 9.0, 8 / 9.0, 5 / 9.0]
    a_ = []
    # print(a_)
    for j in range(m + 1):
        a_.append((2 * (1 - values[j] ** 2)) / (((m + 1) ** 2) * p_[j] ** 2))

    sum_ = 0
    x__ = []
    for j in range(m + 1):
        sum_ += a_[j] * phi((b - a) * values[j] / 2 + (b + a) / 2)
        x__.append((b - a) * values[j] / 2 + (b + a) / 2)

    print('\nУзлы', x__)
    print('Коэффициенты A_k', a_)
    return ((b - a) / 2) * sum_


# Определёный интеграл от a до b
def def_int(func, a, b):
    int__ = lambdify(x, integrate(func, x))
    return int__(b) - int__(a)


# Правило Крамера
def kramer(A, b):
    n, m = A.shape  # размеры массива
    if n == m == len(b):
        solution = [0] * n
        det_A = np.linalg.det(A)
        for i in range(n):
            B = A.copy()
            B[:, i] = b
            solution[i] = np.linalg.det(B) / det_A
        return solution


r = 1
while r:
    print("Функция phi(x) = cos(x)/x^(1/3):\np(x) = 1/x^(1/3), f(x) = cos(x)\n")
    print("Нижний предел интегрирования, A = 0")
    a = 0
    print("Верхний предел интегрирования, B = 1")
    b = 1
    print("Число промежутков деления, m = 2")
    # m = int(input())
    m = 2

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

    # Средние
    int_ = mid()

    print('\nМетод средних прямоугольников, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))

    # Интерполяционная КФ
    A = 0
    B = 1
    x1 = 1 / 4
    x2 = 3 / 4
    w = (x - x1) * (x - x2)
    d_w = lambda x: -a - b + 2 * x  # производная
    mu0, mu1 = map(def_int, [p(x) * x ** k for k in range(2)], [A] * 2, [B] * 2)

    A1 = (mu0 * x2 - mu1) / (x2 - x1)
    A2 = (mu1 - mu0 * x1) / (x2 - x1)

    int_ = A1 * f(x1) + A2 * f(x2)

    print('\nИнтерполяционная КФ (узлы 1/4, 3/4), J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))

    # Формула Гаусса
    int_ = gauss()
    print('\nФормула Гаусса с 3 узлами, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))

    # КФ типа Гаусса
    A = 0
    B = 1

    # Считаем mu_i
    mu0, mu1, mu2, mu3, mu4, mu5 = map(def_int, [p(x) * x ** k for k in range(6)], [A] * 6, [B] * 6)

    A = np.array([[mu2, mu1, mu0], [mu3, mu2, mu1], [mu4, mu3, mu2]])  # матрица A
    b = np.array([-mu3, -mu4, -mu5])  # свободные члены

    # Вычисляем a_i по правилу Крамера
    [a1, a2, a3] = kramer(A, b)

    # Решаем кубическое уравнение и находим x_i
    array = list(map(re, solve(x ** 3 + a1 * x ** 2 + a2 * x + a3)))

    [x1, x2, x3] = array

    w = (x - x1) * (x - x2) * (x - x3)
    d_w = lambda x: 3 * x ** 2 - 2 * (x1 + x2 + x3) * x + (x1 * x2 + x2 * x3 + x1 * x3)

    A1 = 1 / d_w(x1) * (mu2 - (x2 + x3) * mu1 + x2 * x3 * mu0)
    A2 = 1 / d_w(x2) * (mu2 - (x1 + x3) * mu1 + x1 * x3 * mu0)
    A3 = 1 / d_w(x3) * (mu2 - (x1 + x2) * mu1 + x1 * x2 * mu0)

    print('\nКоэффициенты:', A1, A2, A3)
    print('Узлы:', x1, x2, x3)

    int_ = A1 * f(x1) + A2 * f(x2) + A3 * f(x3)
    print('\nФормула типа Гаусса с 3 узлами, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))

    print("Введите 0 для выхода, 1 для продолжения: ")
    r = int(input())

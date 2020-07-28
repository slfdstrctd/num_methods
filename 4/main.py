print("Приближённое вычисление интеграла по составным квадратурным формулам\nВариант 5\n")


# Вес w(x)
def w(y):
    return 1


# Функция f(x)
def f(y):
    global ty
    if ty == 1:
        return w(y) * 1
    if ty == 2:
        return w(y) * 2 * y
    if ty == 3:
        return w(y) * 4 * (y ** 3) - 2 * y


# Max f^(d_+1) для d = 1, 3
def m_(d_):
    global ty
    if d_ == 1:
        if ty == 1:
            return 0
        if ty == 2:
            return 0
        if ty == 3:
            return 24 * b
    if d_ == 3:
        return 0

    return 0


# Первообразная f
def p_(y):
    global ty
    if ty == 1:
        return y
    if ty == 2:
        return y ** 2
    if ty == 3:
        return y ** 4 - y ** 2


# КФ левых прямоугольников
def left():
    s = 0
    k = 0
    for j in range(m):
        s += values[j][1]
        k += 1
    print('count', k)
    return h * s


# КФ правых прямоугольников
def right():
    s = 0
    k = 0
    for j in range(1, m + 1):
        s = s + values[j][1]
        k += 1
    print('count', k)
    return h * s


# КФ средних прямоугольников
def mid():
    s = 0
    k = 0
    for j in range(m):
        s = s + f(values[j][0] + h / 2)
        k += 1
    print('count', k)
    return h * s


# КФ Трапеций
def trapeze():
    s = 0
    k=0
    for j in range(1, m):
        s += values[j][1]
        k += 1
    print('count', k)
    return h * ((values[0][1] + values[m][1]) / 2 + s)


# КФ Симпсона
def simpson():
    v = []
    s_1 = 0
    s_2 = 0
    for j in range(2 * m + 1):
        x_ = (a + j * h / 2)
        v.append((x_, f(x_)))

    for j in range(1, 2 * m, 2):
        s_1 = s_1 + v[j][1]

    for j in range(2, 2 * m - 1, 2):
        s_2 = s_2 + v[j][1]

    return (h / 6) * (v[0][1] + 4 * s_1 + 2 * s_2 + v[2 * m][1])


r = 1
while r:
    print("Введите номер функции:\n"
          "1) f(x) = 1\n"
          "2) f(x) = 2x\n"
          "3) f(x) = 4x^3 - 2x")

    ty = int(input())

    print("Нижний предел интегрирования, A:")
    a = float(input())

    print("Верхний предел интегрирования, B:")
    b = float(input())

    print("Число промежутков деления, m:")
    m = int(input())

    values = []
    h = (b - a) / m  # длина частичного разбиения

    # Массив узлов и значений функции в них
    for i in range(m + 1):
        xi = (a + i * h)
        values.append((xi, f(xi)))

    print('h =', h)
    print('w(x) =', w(1))
    j_ = p_(b) - p_(a)  # точный интеграл
    print('Точное значение интеграла J = F(B) - F(A) =', j_)

    c = 1 / 2  # const для оценки погрешности
    d = 1  # точность формулы
    int_ = left()  # вычисленный интеграл
    print('\nМетод левых прямоугольников, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))
    err = c * m_(d) * (b - a) * (h ** (d + 1))
    print('Теоретическая погрешность:', err)

    int_ = right()
    print('\nМетод правых прямоугольников, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))
    err = c * m_(d) * (b - a) * (h ** (d + 1))
    print('Теоретическая погрешность:', err)

    int_ = mid()
    c = 1 / 24
    print('\nМетод средних прямоугольников, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))
    err = c * m_(d) * (b - a) * (h ** (d + 1))
    print('Теоретическая погрешность:', err)

    int_ = trapeze()
    c = 1 / 12
    print('\nМетод трапеций, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))
    err = c * m_(d) * (b - a) * (h ** (d + 1))
    print('Теоретическая погрешность:', err)
    c = 1 / 2880
    d = 3

    int_ = simpson()
    print('\nМетод Симпсона, J(h):', int_)
    print('Фактическая погрешность, |J - J(h)|:', abs(j_ - int_))
    err = c * m_(d) * (b - a) * (h ** (d + 1))
    print('Теоретическая погрешность:', err)
    print("Введите 0 для выхода, 1 для продолжения: ")
    r = int(input())

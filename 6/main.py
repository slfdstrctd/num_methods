from math import e, sin, cos
import pandas as pd
from sympy import Symbol, integrate, lambdify

x = Symbol('x')

print("Численные методы решения задачи Коши для обыкновенного дифференциального уравнения\nВариант 5\n")
print('y´(x)= - y(x) + sin(x), y(0)=1')
dy = lambda x, y: - y + sin(x)
y = lambda x: 1 / 2 * (3 * e ** (-x) - cos(x) + sin(x))


def series(x_):
    return 1 - (x_ - x0) + (x_ - x0) ** 2 - 1 / 3 * (x_ - x0) ** 3 + 1 / 24 * (x_ - x0) ** 4 - 1 / 120 * (x_ - x0) ** 5


def def_int(func, a, b):
    int_ = lambdify(x, integrate(func, x))
    return int_(b) - int_(a)


def kf(f_, arr, A, B):
    x_ = list(arr['x'])
    y_ = list(arr['T_n(x)'])
    w = (x - x_[0]) * (x - x_[1]) * (x - x_[2]) * (x - x_[3]) * (x - x_[4])
    d_w = lambda x: (5 * x ** 4 -
                     4 * x ** 3 * (sum(x_)) +
                     3 * x ** 2 * (x_[0] * x_[1] + x_[0] * x_[2] + x_[0] * x_[3] + x_[0] * x_[4] + x_[1] * x_[2] +
                                   x_[1] * x_[3] + x_[1] * x_[4] + x_[2] * x_[3] + x_[2] * x_[4] + x_[3] * x_[4]) -
                     2 * x ** 1 * (x_[0] * x_[1] * x_[2] + x_[0] * x_[1] * x_[3] + x_[0] * x_[1] * x_[4] +
                                   x_[0] * x_[2] * x_[3] + x_[0] * x_[2] * x_[4] + x_[0] * x_[3] * x_[4] +
                                   x_[1] * x_[2] * x_[3] + x_[1] * x_[2] * x_[4] + x_[1] * x_[3] * x_[4] +
                                   x_[2] * x_[3] * x_[4]) +
                     1 * x ** 0 * (
                             x_[0] * x_[1] * x_[2] * x_[3] + x_[0] * x_[1] * x_[2] * x_[4] + x_[0] * x_[1] * x_[4] *
                             x_[3] +
                             x_[0] * x_[4] * x_[2] * x_[3] + x_[4] * x_[1] * x_[2] * x_[3])
                     )

    res = sum(def_int(w / (x - x_[i]) / d_w(x_[i]), A, B) * f_(x_[i], y_[i]) for i in range(5))
    return y_[4] + res


def taylor():
    global df
    df = pd.DataFrame(
        [(x0 + k * h, series(x0 + k * h), abs(series(x0 + k * h) - y(x0 + k * h))) for k in
         range(-2, n + 1)]).rename(columns={0: 'x', 1: 'T_n(x)', 2: '|y - T_n(x)|'}, axis=None)
    return


def adams():
    global df
    for k in range(3, n + 1):
        xi = float(df.tail(1)['x'])
        d = kf(dy, df[-5:], xi, xi + h)
        df = df.append({'x': xi + h, 'T_n(x)': d}, ignore_index=True)

    return


def runge_kutta(xi, yi):
    global df
    for k in range(n):
        k1 = h * dy(xi, yi)
        k2 = h * dy(xi + h / 2, yi + k1 / 2)
        k3 = h * dy(xi + h / 2, yi + k2 / 2)
        k4 = h * dy(xi + h, yi + k3)
        xi += h
        yi += 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        df = df.append({'x': xi, 'y': yi}, ignore_index=True)
        # print(xi, yi)
    return


def euler(xi, yi):
    global df
    for k in range(n):
        yi += h * dy(xi, yi)
        xi += h
        df = df.append({'x': xi, 'y': yi}, ignore_index=True)
        # print(xi, yi)
    return


def euler_mod(xi, yi):
    global df
    for k in range(n):
        yi_2 = yi + h / 2 * dy(xi, yi)
        yi += h * dy(xi + h / 2, yi_2)
        xi += h
        df = df.append({'x': xi, 'y': yi}, ignore_index=True)
    return


def euler_cauchy(xi, yi):
    global df
    for k in range(n):
        t = yi + h * dy(xi, yi)
        yi += h / 2 * (dy(xi, yi) + dy(xi + h, t))
        xi += h
        df = df.append({'x': xi, 'y': yi}, ignore_index=True)
    return


print('h = 0.1\nN = 10')
h = 0.1
n = 10
x0 = 0
y0 = 1

# Точное решение
solution = pd.DataFrame([(x0 + k * h - 2, y(x0 + k * h)) for k in range(-2, n + 1)])
solution = solution.rename(columns={0: 'x', 1: 'y'})
solution.index -= 2
print("\nТаблица значений точного решения")
print(solution)

# Ряд Тейлора
df = pd.DataFrame(columns=['x', 'y'])
taylor()
df.index -= 2
print('\nМетод разложения в р. Тейлора:')
print(df[:5])

# Метод Адамса
df = df[:5]
df = df.drop('|y - T_n(x)|', axis=1)
adams()
df = df.rename(columns={'T_n(x)': 'y'})
df.index -= 2
print('\nЭкстраполяционный метод Адамса:')
print(df[5:])
print('Абс. факт. погрешность метода Адамса для y(x_n):', abs(list(df['y'])[-1] - list(solution['y'])[-1]))
df = df.iloc[0:0]

# Метод Рунге-Кутты
runge_kutta(0, 1)
print('\nМетод Рунге-Кутты:')
df.index += 1
print(df[:n])
print('Абс. факт. погрешность метода Рунге-Кутты для y(x_n):', abs(list(df['y'])[-1] - list(solution['y'])[-1]))
df = df.iloc[0:0]

# Метод Эйлера
euler(0, 1)
print('\nМетод Эйлера:')
df.index += 1
print(df)
print('Абс. факт. погрешность метода Эйлера для y(x_n):', abs(list(df['y'])[-1] - list(solution['y'])[-1]))
df = df.iloc[0:0]

# Модифицированный метод Эйлера
euler_mod(0, 1)
print('\nМодифицированный метод Эйлера:')
df.index += 1
print(df)
print('Абс. факт. погрешность мод. метода Эйлера для y(x_n):', abs(list(df['y'])[-1] - list(solution['y'])[-1]))
df = df.iloc[0:0]

# Метод Эйлера-Коши
euler_cauchy(0, 1)
print('\nМетод Эйлера-Коши:')
df.index += 1
print(df)
print('Абс. факт. погрешность метода Эйлера-Коши для y(x_n):', abs(list(df['y'])[-1] - list(solution['y'])[-1]))
df = df.iloc[0:0]

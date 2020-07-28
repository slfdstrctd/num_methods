from math import e, sin, cos
import pandas as pd
from sympy import Symbol, integrate, lambdify

x = Symbol('x')

h = 0.1
n = 10
x0 = 0


def def_int(func, a, b):
    int_ = lambdify(x, integrate(func, x))
    return int_(b) - int_(a)


def formula(f_, arr, A, B):
    x_ = list(arr['x'])
    y_ = list(arr['Tn(x)'])
    omega = (x - x_[0]) * (x - x_[1]) * (x - x_[2]) * (x - x_[3]) * (x - x_[4])
    d_omega = lambda x: (5 * x ** 4 -
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

    gauss_type = sum(def_int(omega / (x - x_[i]) / d_omega(x_[i]), A, B) * f_(x_[i], y_[i]) for i in range(5))
    return y_[4] + gauss_type


dy = lambda x, y: - y + sin(x)
y = lambda x: 1 / 2 * (3 * e ** (-x) - cos(x) + sin(x))

exact = pd.DataFrame([(x0 + k * h, y(x0 + k * h)) for k in range(-2, n + 1)])
exact = exact.rename(columns={0: 'x', 1: 'y(x)'})
print("Таблица значений y(x)")
print(exact)

x0 = 0
taylor_formula = lambda x_: 1 - (x_ - x0) + (x_ - x0) ** 2 - 1 / 3 * (x_ - x0) ** 3 + 1 / 24 * (
            x_ - x0) ** 4 - 1 / 120 * (x_ - x0) ** 5

taylor_table = pd.DataFrame(
    [(x0 + k * h, taylor_formula(x0 + k * h), abs(taylor_formula(x0 + k * h) - y(x0 + k * h))) for k in
     range(-2, n + 1)])
taylor_table = taylor_table.rename(columns={0: 'x', 1: 'Tn(x)', 2: '|y(x) - Tn(x)|'})
print(taylor_table[:5])

f = lambda x, y: - y + sin(x)
adams_table = taylor_table[:5]
adams_table = adams_table.drop('|y(x) - Tn(x)|', axis=1)
# adams_table = adams_table.rename(columns={'Tn(x)': 'f(x)'})

for k in range(3, n + 1):
    xi = float(adams_table.tail(1)['x'])
    d = formula(f, adams_table[-5:], xi, xi + h)
    adams_table = adams_table.append({'x': xi + h, 'Tn(x)': d}, ignore_index=True)
    # print([xi + h, d])
# print(adams_table['f(x)'][-
adams_table = adams_table.rename(columns={'Tn(x)': 'y(x)'})
print(abs(list(adams_table['y(x)'])[-1] - list(exact['y(x)'])[-1]))
# print(adams_table[5:])

yi = 1
xi = 0
runge_kutta_table = pd.DataFrame(columns=['x', 'y(x)'])
for k in range(n):
    k1 = h * dy(xi, yi)
    k2 = h * dy(xi + h / 2, yi + k1 / 2)
    k3 = h * dy(xi + h / 2, yi + k2 / 2)
    k4 = h * dy(xi + h, yi + k3)
    xi += h
    yi += 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    runge_kutta_table = runge_kutta_table.append({'x': xi, 'y(x)': yi}, ignore_index=True)
    # print(xi, yi)
print(abs(list(runge_kutta_table['y(x)'])[-1] - list(exact['y(x)'])[-1]))
print(runge_kutta_table)

yi = 1
xi = 0
euler_table = pd.DataFrame(columns=['x', 'y(x)'])
for k in range(n):
    yi += h * dy(xi, yi)
    xi += h
    euler_table = euler_table.append({'x': xi, 'y(x)': yi}, ignore_index=True)
    # print(xi, yi)
print(abs(list(euler_table['y(x)'])[-1] - list(exact['y(x)'])[-1]))
print(euler_table)

yi = 1
xi = 0
modified_euler_table = pd.DataFrame(columns=['x', 'y(x)'])
for k in range(n):
    yi_2 = yi + h / 2 * dy(xi, yi)
    yi += h * dy(xi + h / 2, yi_2)
    xi += h
    modified_euler_table = modified_euler_table.append({'x': xi, 'y(x)': yi}, ignore_index=True)
    # print(xi, yi)
print(abs(list(modified_euler_table['y(x)'])[-1] - list(exact['y(x)'])[-1]))
print(modified_euler_table)

yi = 1
xi = 0
euler_cauchy_table = pd.DataFrame(columns=['x', 'y(x)'])
for k in range(n):
    Yi = yi + h * dy(xi, yi)
    yi += h / 2 * (dy(xi, yi) + dy(xi + h, Yi))
    xi += h
    euler_cauchy_table = euler_cauchy_table.append({'x': xi, 'y(x)': yi}, ignore_index=True)
    # print(xi, yi)
print(abs(list(euler_cauchy_table['y(x)'])[-1] - list(exact['y(x)'])[-1]))
print(euler_cauchy_table)

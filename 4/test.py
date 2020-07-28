import math
import random

from numpy import arange


# def get_i():
#     return math.e ** 1 - math.e ** 0


def method_of_rectangles(func, mim_lim, max_lim, delta):
    def integrate(func, mim_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - mim_lim) / n
        for x in arange(mim_lim, max_lim - step, step):
            integral += step * func(x + step / 2)
        return integral

    d, n = 1, 1
    while math.fabs(d) > delta:
        d = (integrate(func, mim_lim, max_lim, n * 2) - integrate(func, mim_lim, max_lim, n)) / 3
        n *= 2

    a = math.fabs(integrate(func, mim_lim, max_lim, n))
    b = math.fabs(integrate(func, mim_lim, max_lim, n)) + d
    if a > b:
        a, b = b, a
    print('Rectangles:')
    print('\t%s\t%s\t%s' % (n, a, b))


def trapezium_method(func, mim_lim, max_lim, delta):
    def integrate(func, mim_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - mim_lim) / n
        for x in arange(mim_lim, max_lim - step, step):
            integral += step * (func(x) + func(x + step)) / 2
        return integral

    d, n = 1, 1
    while math.fabs(d) > delta:
        d = (integrate(func, mim_lim, max_lim, n * 2) - integrate(func, mim_lim, max_lim, n)) / 3
        n *= 2

    a = math.fabs(integrate(func, mim_lim, max_lim, n))
    b = math.fabs(integrate(func, mim_lim, max_lim, n)) + d
    if a > b:
        a, b = b, a
    print('Trapezium:')
    print('\t%s\t%s\t%s' % (n, a, b))


def simpson_method(func, mim_lim, max_lim, delta):
    def integrate(func, mim_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - mim_lim) / n
        for x in arange(mim_lim + step / 2, max_lim - step / 2, step):
            integral += step / 6 * (func(x - step / 2) + 4 * func(x) + func(x + step / 2))
        return integral

    d, n = 1, 1
    while math.fabs(d) > delta:
        d = (integrate(func, mim_lim, max_lim, n * 2) - integrate(func, mim_lim, max_lim, n)) / 15
        n *= 2

    a = math.fabs(integrate(func, mim_lim, max_lim, n))
    b = math.fabs(integrate(func, mim_lim, max_lim, n)) + d
    if a > b:
        a, b = b, a
    print('Simpson:')
    print('\t%s\t%s\t%s' % (n, a, b))


def monte_karlo_method(func, n):
    in_d, out_d = 0., 0.
    for i in range(n):
        x, y = random.uniform(0, 1), random.uniform(0, 3)
        if y < func(x):
            in_d += 1

    print('M-K:')
    print('\t%s\t%s' % (n, math.fabs(in_d / n * 3)))


print('as')
method_of_rectangles(lambda x: 4 * (x ** 3) - 2 * x, 0.0, 1.0, 0.001)
trapezium_method(lambda x: 4 * (x ** 3) - 2 * x, 0.0, 1.0, 0.001)
simpson_method(lambda x: 4 * (x ** 3) - 2 * x, 0.0, 1.0, 0.001)
# monte_karlo_method(lambda x: math.e ** x, 100)
# print('True value:\n\t%s' % get_i())

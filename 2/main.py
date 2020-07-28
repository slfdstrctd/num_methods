from math import exp

print("Задача алгебраического интерполирования, \nвариант 5\nf(x) = 1 - exp(-2x)\n")
print("Введите a:")
a = float(input())
print("Введите b:")
b = float(input())
print("Введите m:")
m = int(input())
r = 1
while r:
    def f(y):
        return 1 - exp(-2 * y)


    print("Введите n:")
    n = int(input())

    while n > m:
        print("Введите новое n, старое плохое")
        n = int(input())

    print("Введите x:")
    x = float(input())

    values = []
    for i in range(m + 1):
        xi = (a + i * (b - a) / m)
        values.append((abs(x - xi), xi, f(xi)))

    values.sort()
    print(values)


    def div_diff(a_, b_):
        if a_ > b_:
            exit(0)
        if a_ == b_:
            return values[a_][2]
        else:
            return (div_diff(a_ + 1, b_) - div_diff(a_, b_ - 1)) / (values[b_][1] - values[a_][1])


    def newton(z):
        ans = 0
        t = 1
        for k in range(n + 1):
            ans = ans + div_diff(0, k) * t
            t = t * (z - values[k][1])
        return ans


    def mult(k, z):
        t = 1
        for p in range(n + 1):
            if p != k:
                t = t * (z - values[p][1])
                # print("t", t)
        return t


    def lagrange(q):
        ans = 0
        for t in range(n + 1):
            ans = ans + (values[t][2] * mult(t, q) / mult(t, values[t][1]))
            print('ans', ans)
        return ans


    print("N(x)", newton(x))
    print(f(x))
    print("погрешность метода Ньютона в точке x:", abs(f(x) - newton(x)))

    print("L(x)", lagrange(x))
    print(f(x))
    print("погрешность метода Лагранжа в точке x:", abs(f(x) - lagrange(x)))
    print("Введите 0 для выхода, 1 для продолжения: ")
    r = int(input())

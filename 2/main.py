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
        # return 2 * y ** 3 - 5 * y ** 2 + 3 * y - 1
        
        
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


    def RR(a, b):
        if a > b:
            exit(0)
        if a == b:
            return values[a][2]
        else:
            return (RR(a + 1, b) - RR(a, b - 1)) / (values[b][1] - values[a][1])


    def Newton(z):
        ans = 0
        nakop = 1
        for k in range(n + 1):
            ans += RR(0, k) * nakop
            nakop *= (z - values[k][1])
        return ans


    def zek(k, z):
        nakop = 1
        for p in range(n + 1):
            if p != k:
                nakop *= (z - values[p][1])
                # print("nakop", nakop)
        return nakop


    def Lagrange(q):
        ans = 0
        for t in range(n + 1):
            ans += values[t][2] * zek(t, x) / zek(t, values[t][1])
        return ans


    print("N(x)", Newton(x))
    print(f(x))
    print("погрешность метода Ньютона в точке x:", abs(f(x) - Newton(x)))

    print("L(x)", Lagrange(x))
    print(f(x))
    print("погрешность метода Лагранжа в точке x:", abs(f(x) - Lagrange(x)))
    print("Введите 0 для выхода, 1 для продолжения: ")
    r = int(input())

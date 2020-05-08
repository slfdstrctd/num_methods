print("Задача обратного интерполирования\nвариант 5\nf(x) = 3x^3 + 2x^2 - 4\n")
print("Начало отрезка, a:")
a = float(input())
print("Конец отрезка, b:")
b = float(input())
print("Число значений в таблице, m+1:")
m = int(input()) - 1
r = 1


def f(y):
    return 3 * y ** 3 + 2 * y ** 2 - 4


print("Введите искомое значение функции, F:")
F = float(input())

print("Степень интерполяционного многочлена (n<=m),  n:")
n = int(input())

while n > m:
    print("Введите новое n, старое плохое")
    n = int(input())

values = []
for i in range(m + 1):
    xi = (a + i * (b - a) / m)
    values.append((abs(F - f(xi)), f(xi), xi))


# values.sort()


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
        ans += values[t][2] * zek(t, F) / zek(t, values[t][1])
    return ans


print('i  |  y_i  |  f^(-1)(y_i)')
for i in range(len(values)):
    print(str(i + 1) + ')', values[i][0], '|', values[i][1], '|', values[i][2])

X = Newton(F)
print('\n(Метод Ньютона): X =', X)
print('f(X)=', f(X))
r = f(X) - F
print('r_n(X) =', abs(r))

X = Lagrange(F)

print('\n(Метод Лагранжа): X =', X)
print('f(X)=', f(X))
r = f(X) - F
# print(r)
print('r_n(X) =', abs(r))

# 1 7 10 900 9

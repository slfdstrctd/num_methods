from math import exp

print("Нахождение производных по формулам численного дифференцирования\nВариант 5\nf(x) = exp(1.5 * x)")
r = 1
values = []


# Исходная функция
def f(y):
    return exp(1.5 * y)


# Первая производная (точная)
def f_(j):
    return 1.5 * values[j][1]


# Вторая производная (точная)
def f__(j):
    return 2.25 * values[j][1]


# Первая производная (ЧД)
def f_c(j):
    global values, h
    if j == 0:
        return (-3 * values[j][1] + 4 * values[j + 1][1] - values[j + 2][1]) / (2 * h)
    if j == m:
        return (3 * values[j][1] - 4 * values[j - 1][1] + values[j - 2][1]) / (2 * h)
    return (values[j + 1][1] - values[j - 1][1]) / (2 * h)


# Вторая производная (ЧД)
def f__c(j):
    global values, h
    return (values[j + 1][1] - 2 * values[j][1] + values[j - 1][1]) / (h * h)


while r:
    print("Начало отрезка, a:")
    a = float(input())
    print("Число значений в таблице, m+1:")
    m = int(input()) - 1
    print("Шаг, h:")
    h = float(input())

    for i in range(m + 1):
        xi = (a + i * h)
        values.append((xi, f(xi)))

    # Вывод таблицы значений
    print('\ni |  x_i  |  f(x_i)')
    for i in range(len(values)):
        print(str(i + 1) + ' |', values[i][0], '|', values[i][1])

    print("%-5s%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % (
        '\ni', 'x_i', 'f\'(x_i)T', 'f\'(x_i)ЧД', '|f\'(x_i)-f\'(x_i)ЧД|', 'f\'\'(x_i)', 'f\'\'(x_i)ЧД',
        '|f\'\'(x_i)-f\'\'(x_i)ЧД|'))

    for i in range(m + 1):
        if i == 0 or i == m:
            print("%-5s%-20f%-20f%-20f%-20f%-20f%-20s%-20s" % (
                str(i + 1), values[i][0], f_(i), f_c(i), abs(f_(i) - f_c(i)), f__(i), '——', '——'))
        else:
            print("%-5s%-20f%-20f%-20f%-20f%-20f%-20f%-20f" % (
                str(i + 1), values[i][0], f_(i), f_c(i), abs(f_(i) - f_c(i)), f__(i), f__c(i), abs(f__(i) - f__c(i))))

    print("Введите 0 для выхода, 1 для продолжения: ")
    r = int(input())

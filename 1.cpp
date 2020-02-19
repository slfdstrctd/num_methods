#include <iostream>
#include <cmath>
#include <string>
#include <iomanip>
#include <conio.h>

#define N 100 // max root count
#define R 10 // sphere radius
#define P 0.4 // sphere density

using namespace std;

double **roots;

double A = 0, // or -2 interval start
        B = 2 * R, // or 10 interval end
        h = 0.01, // tabulation step
        eps = pow(10, -7); // accuracy

double (*f)(double x), (*df)(double x);

double f1(double x) {
    return x * sin(x) - 1;
}

double df1(double x) {
    return sin(x) + x * cos(x);
}

double f2(double d) {
    return pow(d, 3) - 3 * pow(d, 2) * R + 4 * pow(R, 3) * P;
}

double df2(double d) {
    return 3 * pow(d, 2) - 6 * R * d;
}

int sgn(double x) {
    return (x > 0) ? 1 : ((x < 0) ? -1 : 0);
}

int root_sep(double a, double b) {
    cout << "[Roots separation]\n";
    roots = new double *[N];

    for (int i = 0; i < N; i++)
        roots[i] = new double[2];

    int k = 0;
    double x1 = a, x2 = x1 + h, y1 = f(x1), y2;

    while (x2 <= b) {
        y2 = f(x2);
        if (y1 * y2 < 0) {
            roots[k][0] = x1;
            roots[k][1] = x2;
            ++k;
//            cout << k << " - x1 = " << x1 << ", x2 = " << x2 << endl;// << ", y1 = " << y1 << ", y2 = " << y2 << endl;
        }
        x1 = x2;
        x2 = x1 + h;
        y1 = y2;
    }
    cout << "Found " << k << " intervals\n";
    return k;
}

void bisection(double a, double b) {
    double x = (double) (a + b) / 2;
    double d = 0;
    int k = 0;

    if (f(a) == 0) cout << setprecision(15) << "Root is " << a << endl;
    if (f(b) == 0) cout << setprecision(15) << "Root is " << a << endl;

    while ((b - a) > eps) {
        d = (b - a) / 2;
        x = a + d;
        if (sgn(f(a)) != sgn(f(x)))
            b = x;
        else a = x;
        ++k;
    }

    cout << setprecision(15) << "Root is " << x << ", accuracy: " << eps << ", obtained: " << k
         << " steps, last interval length: "
         << fabs(b - a) << ", discrepancy: " << fabs(f(x) - 0) << endl << endl;
}

void newton(double a) {
    int k = 0;
    double x1 = a - f(a) / df(a);

    while (fabs(x1 - a) > eps) {
        a = x1;
        x1 = a - f(a) / df(a);
        ++k;
    }
    cout << setprecision(15) << "Root is " << x1 << ", accuracy: " << eps << ", obtained: " << k
         << " steps, last interval length: "
         << fabs(x1 - a) << ", discrepancy: " << fabs(f(x1) - 0) << endl << endl;
}

void newton_mod(double a) {
    int k = 0;
    double dy = df(a), x1 = a - f(a) / dy;

    while (fabs(x1 - a) > eps) {
        a = x1;
        x1 = a - f(a) / dy;
        ++k;
    }

    cout << setprecision(15) << "Root is " << x1 << ", accuracy: " << eps << ", obtained: " << k
         << " steps, last interval length: "
         << fabs(x1 - a) << ", discrepancy: " << fabs(f(x1) - 0) << endl << endl;
}

void secant(double a, double b) {
    int k = 0;
    while (fabs(b - a) > eps) {
        a = b - (b - a) * f(b) / (f(b) - f(a));
        b = a + (a - b) * f(a) / (f(a) - f(b));
        ++k;
    }

    cout << setprecision(15) << "Root is " << b << ", accuracy: " << eps << ", obtained: " << k
         << " steps, last interval length: "
         << fabs(b - a) << ", discrepancy: " << fabs(f(b) - 0) << endl << endl;
}

int main() {
    int t, j;
    string F_1 = "x*sin(x)-1", // f1 name
            F_2 = "d^3 - 3*R*d^2 + 4*R^3*P"; // f2 name

    cout << "Numerical methods for solving non-linear equations\n";
    cout << "Please enter interval start A, interval end B and tabulation parameter h:\n";
    cin >> A >> B >> h;

    cout << "\nInitial values:\nA = " << A << "\nB = " << B
         << "\nep = " << eps << "\nR = " << R << "\nP = " << P << "\nf_1 = " << F_1 << "\nf_2 = " << F_2;

    cout << "\n\nFunctions:\n1 - f_1 = " << F_1 << "\n2 - f_2 = " << F_2 << "\nPlease choose function:\n";
    cin >> t;

    if (t == 1) {
        f = f1;
        df = df1;
    } else {
        f = f2;
        df = df2;
    }

    int k = root_sep(A, B), i = 0;


    do {
        for (j = 0; j < k; ++j) {
            cout << j + 1 << " - x1 = " << roots[j][0] << ", x2 = " << roots[j][1] << endl;
        }

        cout << "Please choose the interval (or 0 to exit):\n";
        cin >> i;
        if (!i) break;

        i--;
        cout << "\n\nMethods:\n1 - Bisection\n2 - Newton's method\n3 - Newton's modified\n4 - Secant method\n"
                "Please choose one:\n";
        cin >> t;


        switch (t) {
            case 1:
                cout << "\n[Bisection]\n";
//            while (i < k) {
                cout << "Initial approximation: x1 = " << roots[i][0] << ", x2 = " << roots[i][1] << endl;
                bisection(roots[i][0], roots[i][1]);
//                ++i;
//            }
                break;
            case 2:
                cout << "\n[Newton's]\n";
//            while (i < k) {
                cout << "Initial approximation: x0 = " << roots[i][0] << endl;
                newton(roots[i][0]);
//                ++i;
//            }
                break;
            case 3:
                cout << "\n[Newton's modified]\n";
//            while (i < k) {
                cout << "Initial approximation: x0 = " << roots[i][0] << endl;
                newton_mod(roots[i][0]);
//                ++i;
//            }
                break;
            case 4:
                cout << "\n[Secant]\n";
//            while (i < k) {
                cout << "Initial approximation: x1 = " << roots[i][0] << ", x2 = " << roots[i][0] << endl;
                secant(roots[i][0], roots[i][1]);
//                ++i;
//            }
                break;
            default:
                break;
        }
        cout << "Press any key to continue...\n";
        getch();
    } while (i != 0);
    return 0;
}
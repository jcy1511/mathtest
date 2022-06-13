from sympy import *
import matplotlib.pyplot as plt


def integral(fx, a, b):
    x = Symbol('x')
    fx = sympify(fx)
    dx_list = []
    fx_list = []
    for dx in range(300, 0, -1):
        i = 0
        sum = 0
        while a+i < b:
            sum += ((dx*0.01)*fx.subs(x, a+i))
            i += dx*0.01
        print(f"dx : {dx*0.01} | {sum}")
        dx_list.append(dx*-0.01)
        fx_list.append(sum)
    plt.plot(dx_list, fx_list)
    plt.show()


integral("3*x**2", 0, 4)

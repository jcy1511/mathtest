from sympy import *
import matplotlib.pyplot as plt


x = Symbol('x')


def differential(fx, xp):
    fxp = fx.subs(x, xp)
    h = 10
    attempts = 0
    limfx = 0
    h_list = []
    limfx_list = []
    while (fx.subs(x, xp+h)-fxp)/h != limfx and h > -10:
        limfx = (fx.subs(x, xp+h)-fxp)/h
        attempts += 1
        print('%20.16f' % limfx, f"| h : {'%.2f'%h} | attempts : {attempts}")
        h_list.append(h)
        limfx_list.append(limfx)
        # h = round(h*0.9, 10)
        h = h-0.01
    print("근사치에 도달하였습니다")
    plt.plot(h_list, limfx_list, linestyle='solid',
             color='red', label=f"(f({xp}+h)-f({xp}))/h")
    plt.plot([-10, 10], [36, 36], linestyle='solid',
             color='blue', label="y=36")
    plt.legend()
    plt.show()

    # p1 = plot(fx, line_color='red', xlim=[-6, 6], ylim=[-6, 6], show=False)
    # p2 = plot(, line_color='red', xlim=[-6, 6], ylim=[-6, 6], show=False)


differential(3*x**3, 2)

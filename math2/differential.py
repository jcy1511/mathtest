from sympy import *
x = Symbol('x')


def differential(fx, xp):
    fxp = fx.subs(x, xp)
    h = 1
    attempts = 0
    limfx = 0
    while (fx.subs(x, xp+h)-fxp)/h != limfx and h > 0:
        limfx = (fx.subs(x, xp+h)-fxp)/h
        attempts += 1
        print('%20.16f' % limfx, f"| h : {'%.3f'%h} | attempts : {attempts}")
        h = round(h-0.001, 3)
    print("근사치에 도달하였습니다")

    # p1 = plot(fx, line_color='red', xlim=[-6, 6], ylim=[-6, 6], show=False)
    # p2 = plot(, line_color='red', xlim=[-6, 6], ylim=[-6, 6], show=False)


differential(3*x**3, 2)

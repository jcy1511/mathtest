from sympy import *
import matplotlib.pyplot as plt


x = Symbol('x')
fig, ax = plt.subplots()
ax.set_ylim(0, 50)
ax.spines['left'].set_position('center')        # 왼쪽 축을 가운데 위치로 이동
ax.spines['right'].set_visible(False)          # 오른쪽 축을 보이지 않도록
ax.spines['top'].set_visible(False)            # 위 축을 보이지 않도록
ax.spines['bottom'].set_position(('data', 0))   # 아래 축을 데이터 0의 위치로 이동
plt.xlabel('h')
plt.ylabel('y')


def differential(fx, xp):
    fxp = fx.subs(x, xp)
    h = 10
    attempts = 0
    limfx = 0
    h_list = []
    limfx_list = []
    while h > -10:
        limfx = (fx.subs(x, xp+h)-fxp)/h
        attempts += 1
        print('%20.16f' % limfx, f"| h : {'%.2f'%h} | attempts : {attempts}")
        h_list.append(h)
        limfx_list.append(limfx)
        h = round(h-0.01, 2)

    plt.plot(h_list, limfx_list, linestyle='solid',
             color='red', label=f'y=f({xp}+h)-f({xp})/h')
    plt.legend()
    plt.show()


differential(3*x**3, 2)

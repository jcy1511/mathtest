from sympy import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(0, 150)
ax.spines['left'].set_position('center')        # 왼쪽 축을 가운데 위치로 이동
ax.spines['right'].set_visible(False)          # 오른쪽 축을 보이지 않도록
ax.spines['top'].set_visible(False)            # 위 축을 보이지 않도록
ax.spines['bottom'].set_position(('data', 0))   # 아래 축을 데이터 0의 위치로 이동
plt.xlabel('h')
plt.ylabel('y')


def integral(fx, a, b):
    x = Symbol('x')
    fx = sympify(fx)
    h_list = []
    fx_list = []

    for h in range(300, 0, -1):
        i = 0
        sum = 0
        while a+i < b:
            sum += fx.subs(x, a+i)*(h*0.01)
            i += h*0.01
        print(f"h : {h*0.01} | {sum}")
        h_list.append(h*0.01)
        fx_list.append(sum)

    plt.plot(h_list, fx_list, linestyle='solid',
             color='blue', label='y=sum')
    plt.plot(h_list, fx_list)
    plt.legend()
    plt.show()


integral("3*x**2", 0, 4)

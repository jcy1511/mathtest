import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('default')
# plt.rcParams['figure.figsize'] = (6, 3)
# plt.rcParams['font.size'] = 12


fig, ax = plt.subplots()

# ax.set_title('Mean Squared Error', pad=20)
# ax.set_xlim(-3, 3)
# ax.set_ylim(0, 3)
# ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
# ax.set_yticks([1, 2, 3])

ax.spines['left'].set_position('center')        # 왼쪽 축을 가운데 위치로 이동
ax.spines['right'].set_visible(False)          # 오른쪽 축을 보이지 않도록
ax.spines['top'].set_visible(False)            # 위 축을 보이지 않도록
ax.spines['bottom'].set_position(('data', 0))   # 아래 축을 데이터 0의 위치로 이동
# ax.tick_params('both', length=0)                # Tick의 눈금 길이 0

x = np.linspace(-3, 3, 100)
# ax.set_xlabel(f'$\frac{}{2}$', fontdict={'fontsize': 14}, labelpad=10)
ax.plot(x, x**2, color='#4799FF', linewidth=5)

plt.show()

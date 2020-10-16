import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [5, 6, 11.1, 7.2, 8.4, 7.6]

plt.plot(x, y,
         marker='o', markersize=12,
         linestyle='dashed', linewidth=2,
         label='series 1', markerfacecolor='red')
plt.title('Position vs Time')
plt.ylabel('Position (m)')
plt.xlabel('Time (s)')
plt.legend()
plt.show()

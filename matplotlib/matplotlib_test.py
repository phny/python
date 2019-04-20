#!/usr/bin/env python3.6

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth = 5)

#设置图表的标题， 并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()

#给定输入和输出值校正图表的显示
#input_values = [1, 2, 3, 4, 5]
#output_values = [1, 4, 9, 16, 25]
#plt.plot(input_values, output_values)
#plt.show()


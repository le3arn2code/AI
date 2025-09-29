import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values, color='lightblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.savefig("bar_chart.png")
plt.close()

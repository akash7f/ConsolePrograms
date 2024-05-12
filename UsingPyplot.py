import matplotlib.pyplot as plt

x = [2, 3, 5, 7, 11]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()

plt.bar(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

plt.pie(x, labels=y, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.show()
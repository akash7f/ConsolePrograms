import numpy as np
import matplotlib.pyplot as plt

#no_of_random values
n = 30

#Generate x values
x = np.linspace(0, 10, n)

#Generate y values with some noise
noise = np.random.normal(0, 1, size=len(x))
y = 2 * x + 1 + noise

plt.scatter(x, y)

#slope, constant,  no of iterations
w = 0
b = 0
n = 100

for i in range(0, n):
    #predicted value
    yh = x*w + b

    #average error
    avg_err = ((yh - y)**2).mean()
    print(avg_err)

    #learning rate
    a = 0.01

    #gradient descent
    #using of engineering convention converter 2*a to a
    w = w - a*(((yh - y)*x).mean())
    b = b - a*((yh - y).mean())



plt.plot(x, yh, label=f"y = {w}*x + {b}")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

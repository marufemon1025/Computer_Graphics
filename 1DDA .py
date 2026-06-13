import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

x_points = []
y_points = []

for i in range(steps + 1):
    x_points.append(round(x))
    y_points.append(round(y))

    x += x_inc
    y += y_inc

plt.plot(x_points, y_points, marker='o')
plt.title("DDA Line Drawing Algorithm")
plt.grid(True)
plt.show()
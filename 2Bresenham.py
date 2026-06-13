import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = abs(x2 - x1)
dy = abs(y2 - y1)

x = x1
y = y1

p = 2 * dy - dx

x_points = []
y_points = []

while x <= x2:
    x_points.append(x)
    y_points.append(y)

    if p < 0:
        p = p + 2 * dy
    else:
        y = y + 1
        p = p + 2 * dy - 2 * dx

    x = x + 1

plt.plot(x_points, y_points, marker='o')
plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.show()
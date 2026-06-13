import matplotlib.pyplot as plt

xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

x = 0
y = r
d = 3 - 2 * r

x_points = []
y_points = []

while x <= y:

    x_points.extend([xc + x, xc - x, xc + x, xc - x,
                     xc + y, xc - y, xc + y, xc - y])

    y_points.extend([yc + y, yc + y, yc - y, yc - y,
                     yc + x, yc + x, yc - x, yc - x])

    if d < 0:
        d = d + 4 * x + 6
    else:
        d = d + 4 * (x - y) + 10
        y = y - 1

    x = x + 1

plt.scatter(x_points, y_points)
plt.title("Bresenham Circle Drawing Algorithm")
plt.axis('equal')
plt.grid(True)
plt.show()
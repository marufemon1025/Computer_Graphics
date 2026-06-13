import matplotlib.pyplot as plt

xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

x = 0
y = r

p = 1 - r

x_points = []
y_points = []

while x <= y:

    x_points.extend([xc + x, xc - x, xc + x, xc - x,
                     xc + y, xc - y, xc + y, xc - y])

    y_points.extend([yc + y, yc + y, yc - y, yc - y,
                     yc + x, yc + x, yc - x, yc - x])

    x += 1

    if p < 0:
        p = p + 2 * x + 1
    else:
        y -= 1
        p = p + 2 * x - 2 * y + 1

plt.scatter(x_points, y_points)
plt.title("Midpoint Circle Drawing Algorithm")
plt.axis('equal')
plt.grid(True)
plt.show()
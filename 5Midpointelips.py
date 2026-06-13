import matplotlib.pyplot as plt
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
rx = int(input("Enter radius along x-axis (rx): "))
ry = int(input("Enter radius along y-axis (ry): "))
x = 0
y = ry
x_points = []
y_points = []
p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
dx = 2 * ry**2 * x
dy = 2 * rx**2 * y
while dx < dy:
    x_points.extend([xc + x, xc - x, xc + x, xc - x])
    y_points.extend([yc + y, yc + y, yc - y, yc - y])
    if p1 < 0:
        x += 1
        dx = 2 * ry**2 * x
        p1 = p1 + dx + ry**2
    else:
        x += 1
        y -= 1
        dx = 2 * ry**2 * x
        dy = 2 * rx**2 * y
        p1 = p1 + dx - dy + ry**2
p2 = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2 * ry**2)
while y >= 0:
    x_points.extend([xc + x, xc - x, xc + x, xc - x])
    y_points.extend([yc + y, yc + y, yc - y, yc - y])
    if p2 > 0:
        y -= 1
        dy = 2 * rx**2 * y
        p2 = p2 - dy + rx**2
    else:
        y -= 1
        x += 1
        dx = 2 * ry**2 * x
        dy = 2 * rx**2 * y
        p2 = p2 + dx - dy + rx**2
plt.scatter(x_points, y_points)
plt.title("Midpoint Ellipse Drawing Algorithm")
plt.axis('equal')
plt.grid(True)
plt.show()
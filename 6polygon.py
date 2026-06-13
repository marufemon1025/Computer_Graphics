import matplotlib.pyplot as plt

x1 = int(input("Enter left x: "))
y1 = int(input("Enter bottom y: "))
x2 = int(input("Enter right x: "))
y2 = int(input("Enter top y: "))
x_points = []
y_points = []
for y in range(y1, y2 + 1):
    for x in range(x1, x2 + 1):
        x_points.append(x)
        y_points.append(y)
plt.scatter(x_points, y_points)
plt.title("Polygon Filling Algorithm")
plt.axis('equal')
plt.grid(True)
plt.show()
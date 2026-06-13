import matplotlib.pyplot as plt

print("Enter the vertices of the triangle:")
print("Enter x1 and y1: ")
x1 = int(input())
y1 = int(input())
print("Enter x2 and y2: ")
x2 = int(input())
y2 = int(input())
print("Enter x3 and y3: ")
x3 = int(input())
y3 = int(input())
print("Enter scaling factors sx and sy: ")
sx = float(input())
sy = float(input())
print("Enter translation values tx and ty: ")
tx = int(input())
ty = int(input())
points = [(x1, y1), (x2, y2), (x3, y3)]
# Scaling
scale_points = [(x * sx, y * sy) for x, y in points]
# Translation
trans_points = [(x + tx, y + ty) for x, y in points]
def plot_polygon(pts, color, label):
    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]
    plt.plot(xs, ys, color=color, marker='o', label=label)
plot_polygon(points, 'blue', 'Original')
plot_polygon(scale_points, 'red', 'Scaled')
plot_polygon(trans_points, 'green', 'Translated')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()

#user input
# x1=0  y1=0
# x2=4  y2=0
# x3=2  y3=4
# sx=2  sy=2
# tx=5  ty=3
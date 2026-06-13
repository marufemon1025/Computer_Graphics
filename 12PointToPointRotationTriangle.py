import matplotlib.pyplot as plt
import math
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
print("Enter the pivot point px and py: ")
px = int(input())
py = int(input())
print("Enter rotation angle (in degrees): ")
angle = float(input())
points = [(x1, y1), (x2, y2), (x3, y3)]
rad = math.radians(angle)
def rotate_about_point(x, y, cx, cy, rad):
    x_t = x - cx
    y_t = y - cy
    x_r = x_t * math.cos(rad) - y_t * math.sin(rad)
    y_r = x_t * math.sin(rad) + y_t * math.cos(rad)
    return x_r + cx, y_r + cy
rot_points = [rotate_about_point(x, y, px, py, rad) for x, y in points]
def plot_polygon(pts, color, label):
    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]
    plt.plot(xs, ys, color=color, marker='o', label=label)
plot_polygon(points, 'blue', 'Original')
plot_polygon(rot_points, 'red', 'Rotated')
plt.scatter([px], [py], color='black', marker='+', s=200, zorder=5, label='Pivot Point')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()

#User Input
# x1=2  y1=2
# x2=6  y2=2
# x3=4  y3=6
# px=4  py=4
# angle=60
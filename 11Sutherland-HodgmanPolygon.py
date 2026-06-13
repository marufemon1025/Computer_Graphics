import matplotlib.pyplot as plt

print("Enter the clipping window xmin and ymin: ")
xmin = int(input())
ymin = int(input())
print("Enter the clipping window xmax and ymax: ")
xmax = int(input())
ymax = int(input())
print("Enter the number of polygon vertices: ")
n = int(input())
vertices = []
for i in range(n):
    print(f"Enter x{i+1} and y{i+1}: ")
    x = float(input())
    y = float(input())
    vertices.append((x, y))
def inside(p, edge):
    x, y = p
    if edge == 'left':   return x >= xmin
    if edge == 'right':  return x <= xmax
    if edge == 'bottom': return y >= ymin
    if edge == 'top':    return y <= ymax
def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    if edge == 'left':
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
    elif edge == 'right':
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
    elif edge == 'bottom':
        y = ymin
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
    elif edge == 'top':
        y = ymax
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
    return (x, y)
def clip_polygon(polygon, edge):
    output = []
    if not polygon:
        return output
    for i in range(len(polygon)):
        curr = polygon[i]
        prev = polygon[i - 1]
        if inside(curr, edge):
            if not inside(prev, edge):
                output.append(intersect(prev, curr, edge))
            output.append(curr)
        elif inside(prev, edge):
            output.append(intersect(prev, curr, edge))
    return output
clipped = vertices
for edge in ['left', 'right', 'bottom', 'top']:
    clipped = clip_polygon(clipped, edge)
rect_x = [xmin, xmax, xmax, xmin, xmin]
rect_y = [ymin, ymin, ymax, ymax, ymin]
plt.plot(rect_x, rect_y, 'b-', label='Clipping Window')
orig_x = [v[0] for v in vertices] + [vertices[0][0]]
orig_y = [v[1] for v in vertices] + [vertices[0][1]]
plt.plot(orig_x, orig_y, 'r--', label='Original Polygon')
if clipped:
    clip_x = [v[0] for v in clipped] + [clipped[0][0]]
    clip_y = [v[1] for v in clipped] + [clipped[0][1]]
    plt.fill(clip_x, clip_y, alpha=0.3, color='green')
    plt.plot(clip_x, clip_y, 'g-', linewidth=2, label='Clipped Polygon')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()


#user input
# xmin=20  ymin=20
# xmax=80  ymax=80
# n=4
# x1=10  y1=10
# x2=100 y2=10
# x3=100 y3=100
# x4=10  y4=100
import matplotlib.pyplot as plt

print("Enter the clipping window xmin and ymin: ")
xmin = int(input())
ymin = int(input())
print("Enter the clipping window xmax and ymax: ")
xmax = int(input())
ymax = int(input())
print("Enter the line starting point x1 and y1: ")
x1 = float(input())
y1 = float(input())
print("Enter the line ending point x2 and y2: ")
x2 = float(input())
y2 = float(input())
LEFT   = 1
RIGHT  = 2
BOTTOM = 4
TOP    = 8
def compute_code(x, y):
    code = 0
    if x < xmin:   code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin:   code |= BOTTOM
    elif y > ymax: code |= TOP
    return code
def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False
    while True:
        if not (code1 | code2):
            accept = True
            break
        elif code1 & code2:
            break
        else:
            code_out = code1 if code1 else code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)
    if accept:
        return x1, y1, x2, y2
    return None
rect_x = [xmin, xmax, xmax, xmin, xmin]
rect_y = [ymin, ymin, ymax, ymax, ymin]
plt.plot(rect_x, rect_y, 'b-', label='Clipping Window')
plt.plot([x1, x2], [y1, y2], 'r--', label='Original Line')
result = cohen_sutherland(x1, y1, x2, y2)
if result:
    cx1, cy1, cx2, cy2 = result
    plt.plot([cx1, cx2], [cy1, cy2], 'g-', linewidth=2, label='Clipped Line')
else:
    print("Line is completely outside the clipping window.")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()

#user input
# xmin=10  ymin=10
# xmax=60  ymax=60
# x1=0    y1=0
# x2=80   y2=80
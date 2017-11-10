import math

input_1 = input()
input_2 = input()

x_list = [float(x) for x in input_1.split()]
x1 = x_list[0]
y1 = x_list[1]

y_list = [float(y) for y in input_2.split()]
x2 = y_list[0]
y2 = y_list[1]

distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print("%0.4f" % distance)
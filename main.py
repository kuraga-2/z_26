from math import sqrt
input_data = open('input.txt', 'r') 
data = input_data.readlines()
a = str(data[0])
b = str(data[1])
a = a.split()
b = b.split()
x1 = int(a[0])
y1 = int(a[1])
r1 = int(a[2])
x2 = int(b[0])
y2 = int(b[1])
r2 = int(b[2])


if sqrt((x1 - x2)**2 + (y1 - y2)**2) <= r1 + r2 :
    output_data = open('output.txt', 'w')
    output_data.write('YES')
elif sqrt((x1-x2)**2 + (y1-y2)**2) + r1 >= r2:
    output_data = open('output.txt', 'w')
    output_data.write('NO')
elif sqrt((x1-x2)**2 + (y1-y2)**2) + r2 >= r1:
    output_data = open('output.txt', 'w')
    output_data.write('NO')

else:
    output_data = open('output.txt', 'w')
    output_data.write('NO')


input_data.close()
output_data.close()
with open('input.txt', 'r') as f:
    c = f.read().rstrip().split('\n')

import numpy as np

n = int(c[0])
id = 1
con = 0.3048
pi = 3.14
an = 360
lcb = 77.68

trim = 2.95

z = [i/10 for i in range(-10, 139)]
x = []
t = []

for i in range(n):
    m = int(c[id].split(',')[1])
    xx = round(float(c[id].split(',')[0])*con, 2)

    if len(x) == 0 or xx - x[-1] > 2:
        x.append(xx)

        temp = [j.split(',') for j in c[id+1: id+m+1]]

        ty = [float(j[0])*con for j in temp]
        tz = [float(j[1])*con + trim * pi * (xx - lcb) / an for j in temp]
        
        yy = [round(j, 2) for j in list(np.interp(z, tz, ty))]
        t.append(yy)

    id += (m+1)

with open('output.txt', 'w') as f:
    print(trim, file=f)
    print('\t' + '\t'.join([str(j) for j in x]), file=f)

    for i in range(len(z)):
        print(str(z[i]) + '\t' + '\t'.join([str(j[i]) for j in t]), file=f)

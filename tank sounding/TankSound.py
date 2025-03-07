import os
import numpy as np

z = [i/10 for i in range(1, 139)]
c = []

den = []
cb = []

for i in [os.listdir('tanks')[0]]:
    with open('tanks/' + i, 'r') as f:
        ii = f.read()
        x = ii.strip().split('\n')
        den.append(float(x[0]))
        cb.append(float(x[1]))


        x = [[float(k) for k in j.split(',')] for j in x[3:]]
        fi = [0 for xx in range(7)]
        ls = [xx for xx in x[-1]]
        ls[0] = 13.8

        x.append(ls)
        x.insert(0, fi)

        y = [[z[i]] for i in range(len(z))]

        for j in range(1, len(x[0])):
            z1 = []
            y1 = []

            for k in x:
                z1.append(k[0])
                y1.append(k[j])

            y2 = np.interp(z, z1, y1)

            for k in range(len(y)):
                y[k].append(round(y2[k], 2))

        c.append(y)

        # c.append(ii)

lcg = 68.95
wei = 31917.48321

g = []

for i in range(len(z)):
    mass = wei
    mag = lcg * wei

    for j in c:
        mass += j[i][2]
        mag += j[i][2] * j[i][3]
    
    g.append(mag/mass)
        


with open('output.txt', 'w') as f:
    for i in range(len(g)):
        print(str(z[i]) + '\t' + str(round(g[i], 3)), file=f)
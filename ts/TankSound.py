#   LCG  MCT  TRIM  OFFSET TABLE  HYDROSTATIC TABLE

import os
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
tanks_path = os.path.join(current_dir, 'tanks')

lcf = 77.505
mct = 1028.9
mom = 0
lcg = 68.95

with open(current_dir + '/weid.txt', 'r') as f:
    wd = [[float(j) for j in i.split('\t')] for i in f.read().split('\n')]

    for i in wd:
        mom += (i[0] - lcf) * i[1]

# mom += (lcg-lcf) * 8379


z = [i/10 for i in range(1, 139)]
c = []

den = []
cb = []

vol = 0

with open(current_dir + '/Loading_basic.dat', 'r') as f:
    car = f.read().strip().split('\n')

    nm = []
    pr = []

    for idx, i in enumerate(car):
        if (idx & 1):
            pr.append(float(i))
        else: 
            nm.append(i + '.txt')

with open(current_dir + '/in.txt', 'r') as f:
    wp = [float(i) for i in f.read().split('\n')]

for idx, i in enumerate(wp):
    vol += i
    wp[idx] = vol * 1.025 / 10

fls = os.listdir(tanks_path)

fls = [i for i in fls if i in nm]
fls.sort()

for i in fls:
    with open(tanks_path + '/' + i, 'r') as f:
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

m = []

g = []
mm = []

for idx, i in enumerate(c):
    m.append(i[-1][2] * pr[idx] / 100)
    mom += (i[-1][3] - lcf) * i[-1][2]

for i in range(len(z)):
    mass = wei
    mag = lcg * wei

    for j in c:
        mass += j[i][2]
        # m.append(j[i][2])
        mag += j[i][2] * j[i][3]
    
    g.append(mag/mass)
    mm.append(float(mass))
        

with open(current_dir + '/output.txt', 'w') as f:

    print(round(mom / mct / 100, 2), file=f)

    # print(sum(m), file=f);

    # print(fls, file=f)

    # for i in m:
    #     print(type(i), file=f)

    for i in range(len(g)):
        print(str(z[i]) + '\t' + str(round(g[i], 2)) + '\t' + str(round(mm[i], 2)) + '\t' + str(round(wp[i], 2)), file=f)

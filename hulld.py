with open('input.txt', 'r') as f:
    c = [[round(float(j), 2) for j in i.split('\t')] for i in f.read().split('\n')]

x = [i for i in range(-3, 164)]

w = []

lcg = 0
we = 0

for j in c:
    we += (j[1]-j[0])*(j[2]+j[3])/2

for i in x:
    su = 0

    for j in c:
        if j[0] <= i and j[1] >= i:
            su += (j[2] * (j[1] - i) + j[3] * (i - j[0])) / (j[1] - j[0])

    w.append(round(su, 2))

    lcg += i * su 

lcg /= sum(w)


with open('output.txt', 'w') as f:
    # print(x, file=f)
    print(round(we, 2), file=f)
    print(sum(w), file=f)

    # print('\t'.join(w))

    # for i in w:
    #     print(i, file=f)
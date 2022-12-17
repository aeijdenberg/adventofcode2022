cnt = 0
for line in open('input.txt'):
    line = line.strip()
    a, b = line.split(',')
    aB, bB = a.split('-'), b.split('-')
    aX, aY, bX, bY = int(aB[0]), int(aB[1]), int(bB[0]), int(bB[1])

    sA, sB = set(x for x in range(aX, aY + 1)), set(x for x in range(bX, bY + 1))
    if len(sA & sB):
        cnt += 1
print(cnt)

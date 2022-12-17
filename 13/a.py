cur = []
all = []
for line in open('input.txt'):
    line = line.strip()
    if len(line):
        cur.append(int(line))
    else:
        all.append(cur)
        cur = []
if len(cur):
    all.append(cur)
print(max(sum(x) for x in all))

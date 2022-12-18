lines = [x for x in open('input.txt')]
firstBlank = lines.index('\n')
cols = int(lines[firstBlank - 1].strip().split(' ')[-1])
stacks = [[] for x in range(cols)]
for line in lines[firstBlank - 2::-1]:
    for i in range(cols):
        ps = 1+i*4
        if ps <= len(line) and line[ps] != ' ':
            stacks[i].append(line[ps])
for line in lines[firstBlank+1:]:
    mv, fromX, toY = [int(x) for x in line.strip().split(' ') if x.isnumeric()]
    tmpS = []
    for i in range(mv):
        tmpS.append(stacks[fromX - 1].pop())
    for i in range(mv):
        stacks[toY - 1].append(tmpS.pop())

print(''.join(x.pop() for x in stacks))

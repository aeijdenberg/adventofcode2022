def priority(c):
    if c >= 'a' and c <= 'z':
        return 1 + ord(c) - ord('a')
    else:
        return 1 + 26 + ord(c) - ord('A')

overlaps = []
lines = [line.strip() for line in open('input.txt')]
for i in range(len(lines) // 3):
    overlaps.append(list(set(lines[i*3]) & set(lines[1+i*3]) & set(lines[2+i*3]))[0])
print(sum(priority(x) for x in overlaps))
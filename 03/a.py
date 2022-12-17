def priority(c):
    if c >= 'a' and c <= 'z':
        return 1 + ord(c) - ord('a')
    else:
        return 1 + 26 + ord(c) - ord('A')

overlaps = []
for line in open('input.txt'):
    line = line.strip()

    left, right = line[:len(line)//2], line[len(line)//2:]
    overlaps.append(list(set(left) & set(right))[0])
print(sum(priority(x) for x in overlaps))
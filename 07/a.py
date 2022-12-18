def new_dir():
    return {'dirs': {}, 'files': {}}

root = new_dir()
pwd = [root]
for line in open('input.txt'):
    line = line.strip()
    if line.startswith('$ cd'):
        d = line.split(' ')[-1]
        if d == '/':
            pwd = [root]
        elif d == '..':
            pwd.pop()
        else:
            pwd.append(pwd[-1]['dirs'][d])
    elif line.startswith('$ ls'):
        pass
    elif line.startswith('dir '):
        d = line.split(' ')[-1]
        pwd[-1]['dirs'][d] = new_dir()
    elif len(line):
        sz, fname = line.split(' ')
        pwd[-1]['files'][fname] = int(sz)


def process_sizes(d):
    d['size'] = sum(d['files'].values())
    for child in d['dirs'].values():
        d['size'] += process_sizes(child)
    return d['size']

process_sizes(root)

def walk_dir_sizes(d):
    for child in d['dirs'].values():
        for z in walk_dir_sizes(child):
            yield z
        yield child['size']

print(sum(x for x in walk_dir_sizes(root) if x <= 100000))

import re
from pprint import pprint

with open('7.txt') as f:
    lines = f.readlines()

pwd = '/'
tree = {pwd: ''}

def traverse_tree(tree, pwd, file_size):
    # base case we're at root
    if pwd == '/':
        return

    # recursive case, go up a dir to root
    pwd = re.sub(r'(?:.(?!\/))+$', '', pwd)

    if not tree.get(pwd):
        tree[pwd] = []

    tree[pwd].append(file_size)
    traverse_tree(tree, pwd, file_size)


for line in lines:
    line = line.strip()

    if line.startswith('$ cd '):
        if '/' in line:
            continue
        if '..' in line:
            pwd = re.sub(r'(?:.(?!\/))+$', '', pwd)
            continue
        cd_dir = re.sub(r'\$.cd.', '/', line)
        pwd += '{}'.format(cd_dir)

    if line.startswith('$ ls'):
        continue

    file_size = re.match(r'\d+', line)
    if file_size:
        file_size = int(file_size.group())

        if not tree.get(pwd):
            tree[pwd] = []

        tree[pwd].append(file_size)

        # traverse tree recursively and add file from nested dir
        traverse_tree(tree, pwd, file_size)

# part one
sum_total = 0
for k, v in tree.items():
    if sum(v) < 100000:
        sum_total += sum(v)

print(sum_total)

# part two
total_size = sum(tree['/'])
total_disk_space_avail = 70000000
unused_space = total_disk_space_avail - total_size
update_space_needed = 30000000
delete_dir_size = update_space_needed - unused_space

delete_dirs = []
for k, v in tree.items():
    if sum(v) > delete_dir_size:
        delete_dirs.append(sum(v))

print(min(delete_dirs))

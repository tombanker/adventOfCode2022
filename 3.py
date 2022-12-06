import string

letters = string.ascii_letters
score = 0

with open('3.txt') as f:
    for i in f.readlines():
        line = i.strip()
        first = set(line[:int(len(line)/2)])
        second = set(line[int(len(line)/2):])
        score += letters.index(list(first.intersection(second))[0]) + 1

print(score) # 8233



score = 0
with open('3.txt') as f:
    lines = f.readlines()

for a, b, c in zip(*[iter(lines)]*3):
    a, b, c = set(a.strip()), set(b.strip()), set(c.strip())

    result = a.intersection(b).intersection(c)
    score += letters.index(list(result)[0]) + 1
print(score)

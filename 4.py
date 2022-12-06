with open('4.txt') as f:
    lines = f.readlines()

score = 0
for i in lines:
    a, b = i.strip().split(',')
    a = int(a.split('-')[0]), int(a.split('-')[1])
    b = int(b.split('-')[0]), int(b.split('-')[1])

    if a[1] - a[0] > b[1] - b[0]:
        if b[0] >= a[0] and b[1] <= a[1]:
            score += 1
    else:
        if a[0] >= b[0] and a[1] <= b[1]:
            score += 1

print(score)


score = 0
for i in lines:
    a, b = i.strip().split(',')
    a = int(a.split('-')[0]), int(a.split('-')[1])
    b = int(b.split('-')[0]), int(b.split('-')[1])

    set_a = set(range(a[0], a[1]+1))
    set_b = set(range(b[0], b[1]+1))

    if set_a.intersection(set_b):
        score += 1

print(score)

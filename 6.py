# packet = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


with open('6.txt') as f:
    lines = f.readlines()


packet = lines[0]

for index, i in enumerate(packet):
    if index < 3:
        continue

    current_group = packet[index-4:index]

    if len(set(current_group)) == 4:
        print(index)
        break

# part two
for index, i in enumerate(packet):
    if index < 13:
        continue

    current_group = packet[index-14:index]

    if len(set(current_group)) == 14:
        print(index)
        break

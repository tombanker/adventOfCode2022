most_calories = 0
current_calories = 0
list_of_calories = []
l = []

with open('1.txt') as f:
    for i in f.readlines():

        if i != '\n':
            current_calories += int(i.strip())
        else:
            l.append(current_calories)

            if current_calories > most_calories:
                most_calories = current_calories

            current_calories = 0

# part one
print(most_calories)

# part two
print(sum(sorted(l)[-3:]))

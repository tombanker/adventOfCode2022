import re
import copy

# lazy parsing, I may come back and parse later
stacks_orig = {
    1: ['R','G', 'J', 'B', 'T', 'V', 'Z'],
    2: ['J', 'R', 'V', 'L'],
    3: ['S', 'Q', 'F'],
    4: ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'],
    5: ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'],
    6: ['S', 'W', 'T', 'C', 'H', 'F'],
    7: ['D', 'Z', 'C', 'V', 'F', 'N', 'J'],
    8: ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'],
    9: ['J', 'B', 'W', 'V', 'P']
    }

with open('5.txt') as f:
    lines = f.readlines()

instructions = []
for i in lines:
    if i.startswith('move'):
        amount, from_stack, to_stack = re.findall(r'\d+', i)
        amount, from_stack, to_stack = int(amount), int(from_stack), int(to_stack)
        instructions.append([amount, from_stack, to_stack])

def reorder_stacks(stacks, instructions):
    for info in instructions:
        for i in range(info[0]):
            popped = stacks[int(info[1])].pop()
            stacks[int(info[2])].append(popped)
    return stacks


stacks_copy = copy.deepcopy(stacks_orig)
message = ''
for i in reorder_stacks(stacks_copy, instructions).values():
    message += i[-1]
print(message)


# part two
def reorder_stacks(stacks, instructions):
    for info in instructions:
        new_stack = []
        for i in range(info[0]):
            popped = stacks[info[1]].pop()
            new_stack.insert(0, popped)
        stacks[info[2]].extend(new_stack)

    return stacks

stacks_copy = copy.deepcopy(stacks_orig)
message = ''
for i in reorder_stacks(stacks_copy, instructions).values():
    message += i[-1]
print(message)

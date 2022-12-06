from collections import OrderedDict

score = 0
strategy_guide = OrderedDict({'A': 'X', 'B': 'Y', 'C':'Z'})

with open('2.txt') as f:
    for i in f.readlines():
        opponent_move, your_move = (list((i.strip()).replace(' ', '')))
        your_move_list  = list(strategy_guide.values())

        # initial score based on your selection
        score += your_move_list.index(your_move) + 1

        # draw
        if your_move == strategy_guide[opponent_move]:
            score += 3

        # win
        winning_index = (your_move_list.index(strategy_guide[opponent_move]) + 1) % 3
        if your_move == your_move_list[winning_index]:
            score += 6

print(score)
# 12535


score = 0
strategy_guide = OrderedDict({'A': 'X', 'B': 'Y', 'C':'Z'})

with open('2.txt') as f:
    for i in f.readlines():
        opponent_move, your_move = (list((i.strip()).replace(' ', '')))
        your_move_list  = list(strategy_guide.values())

        # loose
        if your_move == 'X':
            if opponent_move == 'A':
                score += 3
            if opponent_move == 'B':
                score += 1
            if opponent_move == 'C':
                score += 2

        # draw
        if your_move == 'Y':
            score += 3
            if opponent_move == 'A':
                score += 1
            if opponent_move == 'B':
                score += 2
            if opponent_move == 'C':
                score += 3

        # win
        if your_move == 'Z':
            score += 6
            if opponent_move == 'A':
                score += 2
            if opponent_move == 'B':
                score += 3
            if opponent_move == 'C':
                score += 1

print(score)



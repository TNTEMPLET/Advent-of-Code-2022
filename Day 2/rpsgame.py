f = open('/Users/trent.templet/Dev/WebApps/ZTM/Advent-of-Code-2022/Day 2/input.txt', 'r')
input_ml = f.read()

exemplo = """A Y
B X
C Z"""

shapes = {'X': 1, 'Y': 2, 'Z': 3}

def scoring_1(data):
    score = 0

    for x in data:
        for shape in shapes.keys():
            if x[2] == shape:
                score += shapes[shape]
        if x[0] == 'A':
            if x[2] == 'X': # draw
                score += 3
            elif x[2] == 'Y': # win
                score += 6
        elif x[0] == 'B':
            if x[2] == 'Y': # draw
                score += 3
            elif x[2] == 'Z': # win
                score += 6
        elif x[0] == 'C':
            if x[2] == 'Z': # draw
                score += 3
            elif x[2] == 'X': # win
                score += 6
    return score

win_lose = {'X': 0, 'Y': 3, 'Z':6}


def correct_scoring(data):
    score = 0

    for x in data:
        if x[0] == 'A':
            if x[2] == 'X':
                score += 3
            elif x[2] == 'Y':
                score += 3 + 1
            elif x[2] == 'Z':
                score += 6 + 2
        if x[0] == 'B':
            if x[2] == 'X':
                score += 1
            elif x[2] == 'Y':
                score += 3 + 2
            elif x[2] == 'Z':
                score += 6 + 3
        if x[0] == 'C':
            if x[2] == 'X':
                score += 2
            elif x[2] == 'Y':
                score += 3 + 3
            elif x[2] == 'Z':
                score += 6 + 1
    return score

data = input_ml.splitlines()
# data = exemplo.splitline()

print(f'Solution part 1: {scoring_1(data)}')
print(f'Solution part 2: {correct_scoring(data)}')




        





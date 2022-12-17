scores = []
for line in open('input.txt'):
    line = line.strip()
    them, us = 'ABC'.index(line[0]), 'XYZ'.index(line[-1])
    score = us + 1
    if us == them:
        # draw
        score += 3
    elif us == ((them + 1) % 3):
        # win
        score += 6
    else:
        # loss
        pass
    scores.append(score)
print(sum(scores))

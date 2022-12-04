'''
 The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors
 The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

 The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round.
 single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

 What would your total score be if everything goes exactly according to your strategy guide?

 p2:
  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
  what would your total score be if everything goes exactly according to your strategy guide?
'''

with open("F:\Advent2022\inputAdventDay2.txt") as input:
    lines = input.readlines()
    lastline = lines[-1]
    cumTotal = 0
    for line in lines:
        lineTotal = 0
        startArr = line.split()
        oppChoice = startArr[0]
        print(oppChoice)
        yourChoice = startArr[1]
        print(yourChoice)
        if oppChoice == 'A':
            if yourChoice == 'X':
                #lineTotal += 4
                lineTotal += 3
            elif yourChoice == 'Y':
                #lineTotal += 8
                lineTotal += 4
            else:
                #lineTotal += 3
                lineTotal += 8
        elif oppChoice == 'B':
            if yourChoice == 'X':
                #lineTotal += 1
                lineTotal += 1
            elif yourChoice == 'Y':
                #lineTotal += 5
                lineTotal += 5
            else:
                #lineTotal += 9
                lineTotal += 9
        else:
            if yourChoice == 'X':
                #lineTotal += 7
                lineTotal += 2
            elif yourChoice == 'Y':
                #lineTotal += 2
                lineTotal += 6
            else:
                #lineTotal += 6
                lineTotal += 7
        cumTotal += lineTotal
        print(lineTotal)
    print(cumTotal)
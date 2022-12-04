'''
F:\Advent2022\inputAdventDay1.txt
know how many Calories are being carried by the Elf carrying the most Calories.
p2-get the total number of calories from the top 3 elves.

'''
#input = open("F:\Advent2022\inputAdventDay1.txt", "r")
#print(input.readline())

with open("F:\Advent2022\inputAdventDay1.txt") as input:
    lines = input.readlines()
    lastline = lines[-1]
    mostCals = []
    topThree = []
    elfCal = 0
    final = 0
    for line in lines:
        if line.strip():
            #print(line)
            elfCal+= int(line)
        else:
            #print('blank')
            mostCals.append(elfCal)
            #if elfCal > mostCal:
            #   mostCal = elfCal
            elfCal = 0
    print(mostCals)
    i = 0
    while i < 3:
        final += max(mostCals)
        mostCals.remove(max(mostCals))
        i += 1
    print(final)
        
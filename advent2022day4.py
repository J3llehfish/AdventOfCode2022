'''
Every section has a unique ID number, and each Elf is assigned a range of section IDs.

In how many assignment pairs does one range fully contain the other?

part2: 
In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''
with open("F:\Advent2022\inputAdventDay4.txt") as input:
    lines = input.readlines()
    rangeContain = 0
    for line in lines:
        cords = line.split(',')
        print(cords)
        x1 = int(cords[0].split('-')[0])
        x2 = int(cords[0].split('-')[1])
        y1 = int(cords[1].split('-')[0])
        y2 = int(cords[1].split('-')[1])
        print(x1)
        print(x2)
        print(y1)
        print(y2)
        #part 1
        #if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2):
            #rangeContain += 1
        
        #part2
        if (y1 <= x2) and (x1 <= y2):
            rangeContain += 1
        print(rangeContain)
'''
The list of items for each rucksack is given as characters all on a single line. 
A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
'''

def getPrioNum(priority):
    #lowercase a is 97, uppercase A is 65, done throu ord() which turns letter into unicode value. check if the letter given is uppercase or lowercase by subtracting a value to determine if it is greater than 0
    #could have used .isUpper(), oopsie :)
    print("order for: " + priority + " is " + str(ord(priority)))
    if ord(priority) - 96 > 0:
        totalnum = ord(priority) - 96
        print(totalnum)
        return totalnum
    else:
        totalUpperNum = ord(priority) - 38
        print(totalUpperNum)
        return totalUpperNum
with open("F:\Advent2022\inputAdventDay3.txt") as input:
    lines = input.readlines()
    
    lastline = lines[-1]
    cumTotal = 0
    
    totalMatch = 0
    linesStripped = []
    for line in lines:
        linesStripped.append(line.strip())
    iter = iter(linesStripped)
    i = 0
    grouping = []
    while i < len(linesStripped):
        try:
            checkLine = next(iter)
            grouping.append(checkLine)
            print(i)
            print(grouping)
            if (i+1) % 3 == 0:
                print("grouping: " + str(grouping))
                one = grouping[0]
                two = grouping[1]
                three = grouping[2]
                for character in one:
                    if character in two and character in three:
                        cumTotal += getPrioNum(character)
                        break
                grouping.clear()
            #if i == 3:
                #break
        except StopIteration as e:
            print("StopIteration error handled successfully")
        i+= 1
print(cumTotal)
        
        


#commented out part 1
#[:] is the array slice syntax for every element in the array.
#separate into two compartments
#itemArr = list(line.strip())
#l = len(line)
#compOne = line[0:int(l/2)]
#compTwo = line[int(l/2):l]
#find the equal priority


#for prio in compOne:
#matchNum = 0
#if prio in compTwo:
    #either one works, having a func looks a bit cleaner, no?
    #cumTotal += getPrioNum(prio)
    #cumTotal += (ord(prio) - 38 if prio.isupper() else ord(prio) - 96)
    #break

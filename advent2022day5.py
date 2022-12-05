'''
The ship has a giant cargo crane capable of moving crates between stacks. 
To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. 
After the crates are rearranged, the desired crates will be at the top of each stack.

After the rearrangement procedure completes, what crate ends up on top of each stack?
'''
import numpy as np

with open("F:\Advent2022\inputAdventDay5.txt") as input:
    lines = input.readlines()
    totalBoxes = 0
    #9 is the number of rows, 56 is the total number of boxes
    storageArray = np.zeros((9,56),str)
    rowStack = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0
    }
    #print(storageArray)
    #storageArray = [[]]*9
    for line in lines:
        print(line)
        #first instance of crate in a row
        #print(line.find('['))
        #next instance of crate in a row(inclusive to letters following the first found column, so subtract 2)
        #print(line.find('[',checkOne+1,len(line)))
        if line.startswith("move"):
            #produces 3 digits:
            #1st- number of blocks
            #2nd- from bucket
            #3rd- to bucket
            moves = [int(i) for i in line.split() if i.isdigit()]
            numBlocks, originBucket, endingBucket = moves[0], moves[1] -1 , moves[2] - 1
            #commented part 1 solution
            #while numBlocks > 0:
                #value = list(storageArray[originBucket]).pop(0)
                #storageArr = np.delete(storageArray[originBucket], 0)
                #storageArr = np.append(storageArr,'')
                #storageArray[originBucket] = storageArr
                #getRow = list(storageArray[endingBucket]).insert(0,value)
                #storageArr2 = np.insert(storageArray[endingBucket],0,value)
                #storageArr2 = np.delete(storageArr2, len(storageArr))
                #storageArray[endingBucket] = storageArr2
                #numBlocks -= 1
            #part2 solution
            valuesToAdd = []
            while numBlocks > 0:
                value = list(storageArray[originBucket]).pop(0)
                storageArr = np.delete(storageArray[originBucket], 0)
                storageArr = np.append(storageArr,'')
                storageArray[originBucket] = storageArr
                valuesToAdd.append(value)
                numBlocks -= 1
            storageArr2 = np.insert(storageArray[endingBucket],0,valuesToAdd)
            i = 0
            while i < len(valuesToAdd):
                storageArr2 = np.delete(storageArr2, len(storageArr))
                i+= 1
            storageArray[endingBucket] = storageArr2


        elif line.startswith("1"):
            continue
        else:
            #build starting stacks
            pointer = 0
            
            while pointer < len(line):
                if pointer == 0:
                    position = line.find('[')
                else:
                    position = line.find('[',pointer+1,len(line))
                if(position == -1 ):
                    break
                xaxis = position//4
                #storageArray[int(position/4)] = line[position+1]
                storageArray[xaxis][rowStack[xaxis]] = line[position+1]
                rowStack[xaxis] += 1
                pointer = position + 1
    print(storageArray)
    



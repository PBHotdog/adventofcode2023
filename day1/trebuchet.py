#PART 1
#File Functions
def readFile(filePath):
    lines = []
    try:    
        with open(filePath, 'r') as file:
            for line in file:
                lines.append(line.strip())
        return lines
    except FileNotFoundError:
        print("No file found oh fuck!!!!!!!!")
        return None
    except Exception as exception:
        print("Error: {exception}")
    return None

#Parsing/Adding functions

def getFirstAndLastNum(number):
    firstDigit = number[0]
    lastDigit = number[-1]
    if(firstDigit != None and lastDigit != None):
        return ''.join([firstDigit,lastDigit])
    else:
        return ''.join([firstDigit,firstDigit])

def getNumPerLine(linesList):
    numsList = []
    for line in linesList:
        numsList.append(getFirstAndLastNum(''.join(char for char in line if char.isdigit())))
    numsList = [int(num) for num in numsList]    
    return numsList


#Main Functions
def main(): 
    filePath = 'values.txt'
    file = readFile(filePath)
    test = getNumPerLine(file)
    result = sum(test)
    print(result)


if __name__ == "__main__":
    main()
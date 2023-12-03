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
        print("No file found :O")
        return None
    except Exception as exception:
        print("Error: {exception}")
    return None

#Dictionaries
#Replacing stuff because I'm too tired to learn regex again
replacementValues = {
    "zerone": "zeroone",
    "oneight": "oneeight",
    "twone": "twoone",
    "sevenine": "sevennine",
    "eightwo": "eighttwo",
    "eighthree": "eightthree",
    "nineight": "nineeight"
}

convertWordstoNums = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9"
  }
#Parsing/Adding functions
def getFirstAndLastNum(number):
    firstDigit = number[0]
    lastDigit = number[-1]
    if(firstDigit != None and lastDigit != None):
        return ''.join([firstDigit,lastDigit])
    else:
        return ''.join([firstDigit,firstDigit])

def replaceNumsandWeirdValues(line):
    makeLower = line.lower()
    for replaceWeirdValues in replacementValues.keys():
        makeLower = makeLower.replace(replaceWeirdValues, replacementValues[replaceWeirdValues])
    for number in convertWordstoNums:
        makeLower = makeLower.replace(number, convertWordstoNums[number])


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
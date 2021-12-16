import pprint

txt = 'input'
with open(txt) as f:
    lines = [x.strip() for x in f.readlines()]
    for idx, line in enumerate(lines):
        lines[idx] = [item for item in line]

# keeps track of how many errors of each type there are and the cost associated with each error
errorCost = {')':[3,0], ']':[57,0], '}':[1197,0], '>':[25137,0]}

# look up to see if the current opening mathces the current closing
matchingClosed = {')':'(', ']':'[', '}':'{', '>':'<'}
matchingOpened = {'(':')', '[':']', '{':'}', '<':'>'}

#Returns a dictionary, keys are indexes of open and values are false to be set to true when mathcing close later
def getAllOpenedClosed(line, matchingClosed):
    allOpenedClosed = {}
    for idx, item in enumerate(line):
        if item in matchingClosed:
            allOpenedClosed[idx] = [False, 'closed', item]
        else: allOpenedClosed[idx] = [False, 'opened', item]
    return allOpenedClosed

# Checks if there is an error in any given line and updates errorCost
def checkLineError(line, currOpened, errorCost, matchingClosed, matchingOpened, allOpenedClosed):
    for idx, item in enumerate(line):
        if item in matchingClosed and matchingClosed[item] != currOpened[1]:
            errorCost[item][1] += 1
            return (True, errorCost)
        elif item in matchingOpened:
            currOpened = [idx, item]
        elif matchingClosed[item] == currOpened[1]:
            allOpenedClosed[idx][0], allOpenedClosed[currOpened[0]][0] = True, True
            while(True):
                if line[currOpened[0]] in matchingOpened and allOpenedClosed[currOpened[0]][0] == False and allOpenedClosed[currOpened[0]][1] == 'opened':
                    break
                else:
                    if currOpened[0] > 0:
                        currOpened = [currOpened[0]-1, line[currOpened[0]-1]]
                    else: break
    return (False, errorCost)


# Goes through all the lines and checks if there is an error
def checkAllLineErrors(lines, errorCost, matchingClosed, matchingOpened):
    isError = []
    for line in lines:
        allOpened = getAllOpenedClosed(line, matchingClosed)
        isE, errorCost = checkLineError(line, None, errorCost, matchingClosed, matchingOpened, allOpened)
        isError.append(isE)
    return isError, errorCost

#Totals up all the errors
def totalErrorCost(errorCost):
    cost = 0
    for error in errorCost:
        cost += errorCost[error][0] * errorCost[error][1]
    return cost

def getNonErrorLines(lines, isError):
    nonError = []
    for idx, line in enumerate(lines):
        if isError[idx] == False:
            nonError.append(line)
    return nonError

def findMissingSymbols(nonErrorLine, matchingClosed, matchingOpened):
    allOpen = []
    for item in nonErrorLine:
        if item in matchingClosed:
            allOpen.pop(-1)
        else: allOpen.append(item)
    missing = reversed(allOpen)
    missing = [matchingOpened[o] for o in missing]
    return missing
            
def findAllMissingSymbols(nonErrorLines, matchingClosed, matchingOpened):
    allClosedSymbols = []
    for line in nonErrorLines:
        allClosedSymbols.append(findMissingSymbols(line, matchingClosed, matchingOpened))
    return allClosedSymbols

def calcScore(missingSymbols):
    score = 0
    for item in missingSymbols:
        score *= 5
        if item == ')': score += 1
        elif item == ']': score += 2
        elif item == '}': score += 3
        else: score += 4
    return score

def calcAllScores(allMissingSymbols):
    scores = []
    for missingSymbol in allMissingSymbols:
        scores.append(calcScore(missingSymbol))
    return scores

def findMiddleScore(scores):
    scores = sorted(scores)
    return scores[int((len(scores) - 1) / 2)]

isError, errorCost = checkAllLineErrors(lines, errorCost, matchingClosed, matchingOpened)
nonErrorLines = getNonErrorLines(lines, isError)
allMissingSymbols = findAllMissingSymbols(nonErrorLines, matchingClosed, matchingOpened)
scores = calcAllScores(allMissingSymbols)
middleScore = findMiddleScore(scores)

print('The answer to part 2 is ', middleScore)

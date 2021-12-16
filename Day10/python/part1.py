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
    for line in lines:
        allOpened = getAllOpenedClosed(line, matchingClosed)
        _, errorCost = checkLineError(line, None, errorCost, matchingClosed, matchingOpened, allOpened)
    return errorCost

#Totals up all the errors
def totalErrorCost(errorCost):
    cost = 0
    for error in errorCost:
        cost += errorCost[error][0] * errorCost[error][1]
    return cost

errorCost = checkAllLineErrors(lines, errorCost, matchingClosed, matchingOpened)
totalCost = totalErrorCost(errorCost)

print('The answer to part 1 is: ',totalCost, ' with the error dist ',errorCost)
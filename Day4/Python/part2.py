from re import search
import numpy as np
from pprint import pprint

txt = 'input'
with open(txt) as f:
    tmp = f.readlines()
    numbers = tmp[0].strip().split(",")
    numbers = [int(x) for x in numbers]
    cards = []
    for item in tmp[2:]:
        cards.append(item.strip().split())
    tmp = []
    tmpCards = []
    for idx, val in enumerate(cards):
        if val == [] or idx == (len(cards) - 1):
            if idx == len(cards) - 1:
                tmp.append([int(x) for x in val])
            tmpCards.append(tmp)
            tmp = []
        else:
            tmp.append([int(x) for x in val])

cards = np.array(tmpCards)
numbers = np.array(numbers)
statuses = np.zeros_like(cards)


#Check if specific card at index is a winner and append that winners index to winners
# and return the winners
def checkCard(status, idx):
    for line in status:
        if all(line): 
            return idx
    for line in np.transpose(status, (1,0)):
        if all(line): 
            return idx
    return

#Check which cards are winners and return the indices of those winners
def checkWinner(statuses):
    winners = []
    for idx, status in enumerate(statuses):
        curr = checkCard(status, idx)
        if curr != None:
            winners.append(curr)
    return winners

#Mark with a 1 (true) if a number is read that is on that card (assuming no duplicate numbers)
def markCard(card, status, number):
    for idx, line in enumerate(card):
        for i, n in enumerate(line):
            if n == number:
                status[idx, i] = 1
    return status

#Mark all cards with a 1 (true) if a number is read that is on that card (assuming no duplicate numbers)
def markCards(cards, statuses, number):
    for idx, status in enumerate(statuses):
        statuses[idx] = markCard(cards[idx], status, number)
    return statuses

#Read all the numbers and mark the cards then check winner
def readNumbers(cards, statuses, numbers):
    for number in numbers:
        statuses = markCards(cards, statuses, number)
        winners = checkWinner(statuses)
        if len(winners) == len(cards) - 1:
            most_winners = winners
        elif len(winners) == len(cards):
            return winners, cards, number, most_winners
    return winners, cards, number, most_winners

#Sum over all the unmarked numbers in a card
def sumUnMarked(card, status):
    s = 0
    for idx, line in enumerate(status):
        for i, item in enumerate(line):
            if item == 0:
                s += card[idx][i]
    return s

winners, cards, number, most_winners = readNumbers(cards, statuses, numbers)
idxLoser = list(set(winners) - set(most_winners))[0]
s = sumUnMarked(cards[idxLoser], statuses[idxLoser])

#if there are more than one winners then I will just take the first one
print('The sum is: ',s,' and the last number is ',number)
print('The product is: ', s * number, ' and the losing card is number ', idxLoser + 1 )
print('The losing card should be ', cards[idxLoser])
print('The losing status should be ', statuses[idxLoser])
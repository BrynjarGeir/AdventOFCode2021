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
                tmp.append([(int(x), False) for x in val])
            tmpCards.append(tmp)
            tmp = []
        else:
            tmp.append([(int(x), False) for x in val])

cards = np.array(tmpCards)
numbers = np.array(numbers)

#Check if specific card at index is a winner and append that winners index to winners
# and return the winners
def checkCard(card, idx):
    search = 1
    for line in card:
        curr = [e[1] == search for e in line]
        if all(curr): 
            return idx
    for line in np.transpose(card, (1,0,2)):
        curr = [e[1] == search for e in line]
        if all(curr): 
            return idx
    return

#Check which cards are winners and return the indices of those winners
def checkWinner(cards):
    winners = []
    for idx, card in enumerate(cards):
        curr = checkCard(card, idx)
        if curr != None:
            winners.append(curr)
    return winners

#Mark with a 1 (true) if a number is read that is on that card (assuming no duplicate numbers)
def markCard(card, number):
    for idx, line in enumerate(card):
        for i, n in enumerate(line):
            if n[0] == number:
                card[idx][i][1] = 1
    return card

#Mark all cards with a 1 (true) if a number is read that is on that card (assuming no duplicate numbers)
def markCards(cards, number):
    for idx, card in enumerate(cards):
        cards[idx] = markCard(card, number)
    return cards

#Read all the numbers and mark the cards then check winner
def readNumbers(cards, numbers):
    for number in numbers:
        cards = markCards(cards, number)
        winners = checkWinner(cards)
        if winners != []:
            return winners, cards, number
    return 'No winner!'

#Sum over all the unmarked numbers in a card
def sumUnMarked(card):
    s = 0
    for line in card:
        for item in line:
            if item[1] == 0:
                s += item[0]
    return s

winners, cards, number = readNumbers(cards, numbers)
s = sumUnMarked(cards[winners[0]])

#if there are more than one winners then I will just take the first one
print('The sum is: ',s,' and the last number is ',number)
print('The product is: ', s * number, ' and the winning card is number ', winners[0] )
#print('The winning card should be ', cards[14])
inp = input('What data set do you want? ')
with open('../data/'+inp) as f:
    player1, player2 = f.read().split('\n')
    player1 = {'pos':int(player1.split(': ')[1]), 'score':0, 'name':'player1'}; player2 = {'pos':int(player2.split(': ')[1]), 'score':0, 'name':'player2'}

def diracDie(roll): return roll
def playerTurn(roll, player):
    movement = roll + (roll + 1) + (roll + 2)
    pos = (player['pos']+movement)
    while pos > 10: pos -= 10
    player['pos'] = pos
    player['score'] += player['pos']
    return player, roll+3
def findTheWinner(roll, players, goal):
    player1, player2 = players
    while player1['score'] < goal and player2['score'] < goal:
        player1, roll = playerTurn(roll, player1)
        if player1['score'] >= goal: return roll, (player1, player2), 'Player 1 is the winner!'
        player2, roll = playerTurn(roll, player2)
        if player2['score'] > goal: return roll, (player1, player2), 'Player 2 is the winner!'
    return roll, (player1, player2), 'One of them is the winner. This shouldn\'t really happen!'

roll, (player1, player2), winner = findTheWinner(1, (player1, player2), 1000)
if 'Player 1 in winner': print('The answer to part 1 is ',(roll-1)*player2['score'])
else: print('The answer to part 1 is ', (roll-1)*player1['score'])
import random
import sys

player_tickets = []
winning_tickets = []

players = 0
prizes = 0

amt = "Amount of"
nam = "Name"
plr = "players"
prz = "prizes"
tck = "tickets"
ptt = "SELL MORE TICKETS"
see = "See winner"
ext = "Confirm Close"

# Function for registering the amount of players and prizes
def reg(i, m):
    while True:
        try:
            i = int(raw_input("%s %s: " % (amt, m)))
        except ValueError:
            continue
        else:
            return i
            break

players = reg(players, plr)
prizes = reg(prizes, prz)

# Registers players and how many tickets they each have
for x in range(0, players):
    while True:
        try:
            player = raw_input("%s: " % nam)
        except ValueError:
            continue
        else:
            if player == "":
                continue
            break
    while True:
        try:
            tickets = int(raw_input("%s %s: " % (amt, tck)))
        except ValueError:
            continue
        else:
            for x in range(0, tickets):
                player_tickets.append(player)
            break

random.shuffle(player_tickets)

# Picks out the winning tickets
for x in range(0, prizes):
    try:
        winner = player_tickets.pop()
        winning_tickets.append(winner)
    except IndexError:
        raw_input("\n%s!\n" % ptt)
        sys.exit()

# Prints out the winner after each Enter press
for x in winning_tickets:
    raw_input("\n(Enter)%s: \n" % see)
    print x

# Confirms program exit
raw_input("\n %s (Enter)" % ext)

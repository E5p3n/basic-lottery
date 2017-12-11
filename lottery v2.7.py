import random
import sys

plr_tck = []
win_tck = []

amt = "Amount of"
nam = "Name"
plr = "players"
prz = "prizes"
tck = "tickets"
ptt = "SELL MORE TICKETS"
see = "See winner"

# Asks user for the amount of players
while True:
    try:
        players = int(raw_input("%s %s: " % (amt, plr)))
    except ValueError:
        continue
    else:
        break

# Asks user for the amount of prizes
while True:
    try:
        prizes = int(raw_input("%s %s: " % (amt, prz)))
    except ValueError:
        continue
    else:
        break

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
                plr_tck.append(player)
            break

random.shuffle(plr_tck)

# Picks out the winning tickets
for x in range(0, prizes):
    try:
        winner = plr_tck.pop()
        win_tck.append(winner)
    except IndexError:
        print "\n%s!\n" % ptt
        sys.exit()

# Prints out the winner after each Enter press
for x in win_tck:
    raw_input("\n(Enter)%s: \n" % see)
    print x

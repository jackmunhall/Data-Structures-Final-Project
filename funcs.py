import csv

def getBool():
    b = input("PPR? ").lower().strip()
    if b == "yes":
        return True
    else:
        return False

# Calculates a player's worth
def calcWorth(name, playerStats, leagueInfo):
    # leagueInfo = (ppr, numTeams, year, dynasty)
    # rookie bool in playerStats[name][-1]

    player = playerStats[name];

    if leagueInfo[-1]:
        if (player[-1]):
            return calcDynastyRookieWorth(player)
        else:
            return calcDynastyVetWorth(player, leagueInfo)
    else:
        if (player[-1]):
            return calcRedraftRookieWorth(player)
        else:
            return calcRedraftVetWorth(player, leagueInfo)

    return 1

def calcRedraftVetWorth(player, leagueInfo):
    pass

def calcDynastyVetWorth(player, leagueInfo):
    pass

def calcRedraftRookieWorth(player):
    pos = player[3]
    draft_round = int(player[0])

    value = 0

    if position == "QB":
        if draft_round == 1:
            value = 3000
        elif draft_round == 2:
            value = 1500
        elif draft_round == 3:
            value = 500
        elif draft_round == 4 or draft_round == 5:
            value = 200
        elif draft_round == 6 or draft_round == 7:
            value = 100
    else:
        if draft_round == 1:
            value = 1500
        elif draft_round == 2:
            value = 750
        elif draft_round == 3:
            value = 150
        elif draft_round == 4 or draft_round == 5:
            value = 100
        elif draft_round == 6 or draft_round == 7:
            value = 50

def calcDynastyRookieWorth(player):
    pos = player[3]
    draft_round = int(player[0])

    value = 0

    if pos == "QB":
        if draft_round == 1:
            value = 3000
        elif draft_round == 2:
            value = 1500
        elif draft_round == 3:
            value = 500
        elif draft_round == 4 or draft_round == 5:
            value = 200
        elif draft_round == 6 or draft_round == 7:
            value = 100
    else:
        if draft_round == 1:
            value = 1500
        elif draft_round == 2:
            value = 750
        elif draft_round == 3:
            value = 150
        elif draft_round <= 5:
            value = 100
        elif draft_round == 6 or draft_round == 7:
            value = 50

    return value

# Calculates worth ratio between players
def calcFairness(player0, player1):
    # worth is for team 0 trading to team 1

    return player1[1] / player0[1]


# Reads teams out of team0 and team1
def readTeam(f, playerStats, leagueInfo):
    with open(f) as file:
        reader = csv.reader(file)
        team = []

        for row in reader:
            name = row[0]
            worth = calcWorth(name, playerStats, leagueInfo)

            data = (name, worth)
            team.append(data)

    return team

# reads all player stats in and flags rookies - rookie flag can be accessed with stats[name][-1]
def readPlayers(vets, rookies):
    with open(vets) as vF, open(rookies) as rF:
        vRead = csv.reader(vF)
        rRead = csv.reader(rF)

        players = {}

        for row in rRead:
            temp = row[5:]
            for i in range(0, len(temp)):
                try:
                    temp[i] = float(temp[i])
                except:
                    temp[i] = 0

            temp.append(True)
            players[row[3].strip()] = row[0:3] + [row[4]] + temp

        for row in vRead:
            temp = row[2:]
            for i in range(0, len(temp)):
                try:
                    temp[i] = float(temp[i])
                except:
                    temp[i] = 0

            temp.append(False)
            players[row[1].strip()] = temp

    return players

## SUPERCEDED BY readPlayers
# def readFile(f):
#     with open(f) as file:
#         reader = csv.reader(file)
#         players = {}

#         for row in reader:
#             temp = row[2:]
#             for i in range(0, len(temp)):
#                 try:
#                     temp[i] = float(temp[i])
#                 except:
#                     temp[i] = 0

#             players[row[1].strip()] = temp

#     return players

# Matches a player to someone on other team based on worth - looks for most similar pairings
def matchPlayer(player, matches, playerStats):
    for m in matches:
        if not matches[m]:
            f = calcFairness(player, m)
            matches[m] = [player, f]
            break

        fairnessNew = calcFairness(player, m)
        fairnessOld = matches[m][1]

        fNewClose = abs(1 - fairnessNew)
        fOldClose = abs(1 - fairnessOld)

        # print(name,"for",m,fNewClose)

        if fOldClose > fNewClose:
            oldName = matches[m][0]
            matches[m] = [player, fairnessNew]
            matchPlayer(oldName, matches, playerStats)
            break


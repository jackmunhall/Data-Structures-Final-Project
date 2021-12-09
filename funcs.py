import csv

def getBool(s):
    b = s.lower().strip()
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
            print(name, end=' ')
            return calcRedraftVetWorth(player, leagueInfo)

    return 1

def calcRedraftVetWorth(player, leagueInfo):
    value = 0.0
    value = float(value)
    position = player[1]
    touchdowns = float(player[21])
    yards = float(player[7]+player[11]+player[16])
    games_season = 16
    games_played = float(player[3])
    league_scoring = leagueInfo[0];
    #previous years stats
    if position == "QB":
        value = float(0.4*yards) + (55*touchdowns)
    else:
        value = float(yards + (125*touchdowns))
    #fantays points
    if leagueInfo[0]:
        ppr_score = float(player[25])
        value = float(value + (2*ppr_score))
    else:
        standard_score = float(player[24])
        value = float(value + (2*standard_score))

    #availability
    value = float(value*((games_played + 1)/games_season))
    #league settings
    if position == "QB":
      num_QB = float(leagueInfo[4])
      if num_QB == 2:
          value = 1.5*float(value)
    if leagueInfo[1] != 10:
       value = (value*(float(num_teams)/10.0))
    return value

def calcDynastyVetWorth(player, leagueInfo):
    value = 0.0
    value = float(value)
    position = player[1]
    touchdowns = float(player[21])
    yards = float(player[7]+player[11]+player[16])
    games_season = 16
    games_played = float(player[3])
    league_scoring = leagueInfo[0];
    #previous years stats
    if position == "QB":
        value = float(0.4*yards) + (55*touchdowns)
    else:
        value = float(yards + (125*touchdowns))
    #fantays points
    if leagueInfo[0]:
        ppr_score = float(player[25])
        value = float(value + (2*ppr_score))
    else:
        standard_score = float(player[24])
        value = float(value + (2*standard_score))

    #availability
    value = float(value*((games_played + 1)/games_season))
    #league settings
    if position == "QB":
        num_QB = float(leagueInfo[4])
        if num_QB == 2:
            value = 1.5*float(value)
    if leagueInfo[1] != 10:
        value = (value*(float(leagueInfo[1])/10.0))
    #age
    age = float(player[2])
    if position == "QB":
        if age > 37:
            value = value * 0.6
        elif age > 34:
            value = value * 0.7
        elif age > 29:
            value = value * 0.8
        elif age > 25:
            value = value * 0.9
    elif position == "RB":
        if age > 30:
            value = value * 0.6
        elif age > 28:
            value = value * 0.7
        elif age > 25:
            value = value * 0.8
        elif age > 23:
            value = value * 0.9
    elif position == "WR" or position == "TE":
        if age > 32:
            value = value * 0.6
        elif age > 30:
            value = value * 0.7
        elif age > 28:
            value = value * 0.8
        elif age > 24:
            value = value * 0.9
    return value

def calcRedraftRookieWorth(player):
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

def calcPickWorth(name, leagueInfo):
    if not leagueInfo[-2]:
        return 0

    data = name.split()
    data = [int(x) for x in data]

    year = data[1]
    draft_round = data[0]
    curr_year = leagueInfo[2]

    if year == curr_year:
        if draft_round == 1:
            value = 2500
        elif draft_round == 2:
            value = 1250
        elif draft_round == 3:
            value = 500
        else:
            print(f'Inalid input\n')
            quit()
    elif year == (curr_year + 1):
        if draft_round == 1:
            value = 2000
        elif draft_round == 2:
            value = 1000
        elif draft_round == 3:
            value = 350
        else:
            print(f'Inalid input\n')
            quit()
    elif year == (curr_year + 2):
        if draft_round == 1:
            value = 1500
        elif draft_round == 2:
            value = 750
        elif draft_round == 3:
            value = 200

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

            if (name[0].isnumeric()):
                worth = calcPickWorth(name, leagueInfo)
            else:
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
            temp = row[4:]
            for i in range(0, len(temp)):
                try:
                    temp[i] = float(temp[i])
                except:
                    temp[i] = 0

            temp.append(False)
            players[row[1].strip()] = row[2:4] + temp

    return players

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


from funcs import *

# Read in all stats
playerStats = readPlayers("stats.csv", "draft.csv")

# Get basic league info
sPPR = input("PPR? ")
ppr = getBool(sPPR)

numTeams = int(input("Number of teams in the league: "))
year = int(input("Current year: "))
qb = int(input("QBs allowed on team: "))

sDyn = input("Dynasty? ")
dynasty = getBool(sDyn)

# Package leage info
leagueInfo = (ppr, numTeams, year, dynasty, qb)

# Read in teams and calculate their worth
team0 = readTeam("team0.csv", playerStats, leagueInfo)
team1 = readTeam("team1.csv", playerStats, leagueInfo)

print(team0)
print(team1)

matches = dict.fromkeys(team1)

for player in team0:
    matchPlayer(player, matches, playerStats)

print("MATCHES")
for k, v in matches.items():
    if v:
        print("Trading", v[0][0], "for", k[0], "has a bias of {:.2f}".format(v[1]))
    else:
        print(k, "has no match")

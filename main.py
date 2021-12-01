import csv
from funcs import *

players = {}

# Rk	Player	Tm	FantPos	Age	G	GS	Cmp	Att	Yds	TD	Int	Att	Yds	Y/A	TD	Tgt	Rec	Yds	Y/R	TD	Fmb	FL	TD	2PM	2PP	FantPt	PPR	DKPt	FDPt	VBD	PosRank	OvRank
with open("stats.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        temp = row[2:]
        for i in range(0, len(temp)):
            try:
                temp[i] = float(temp[i])
            except:
                temp[i] = None

        players[row[1]] = temp

for p, v in players.items():
    print(p, v)

test = calcWorth(players, "Tom Brady")
print(test)

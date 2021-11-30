import csv

players = {}

# Rk	Player	Tm	FantPos	Age	G	GS	Cmp	Att	Yds	TD	Int	Att	Yds	Y/A	TD	Tgt	Rec	Yds	Y/R	TD	Fmb	FL	TD	2PM	2PP	FantPt	PPR	DKPt	FDPt	VBD	PosRank	OvRank
with open("stats.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        players[row[1]] = row[2:]

for p, v in players.items():
    print(p, v)

def calcWorth(players, name):
    player = players[name];

    pos = player[3]

    tds = player[10] + player[15] + player[20]
    yards = player[9] + player[13] + player[18]

    if pos == 'QB':
        return tds * 55 + yards * .4
    else:
        return tds * 125 + yards


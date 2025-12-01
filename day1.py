# Day 1-1
start = 50
limit = 100
goal = 0
g_count = 0
dial = start
with open('files/1-1-input.txt') as file:
    lines = file.readlines()
for line in lines:
    dir = line[0]
    amt = int(line[1:].strip())
    mult = 1 if dir == 'R' else -1
    dial = (dial + (mult * amt)) % limit
    if dial == goal: g_count += 1
print(g_count)

# Day 1-2
clicks = 0
dial = start
for line in lines:
    dial_start = dial
    dir = line[0]
    amt = int(line[1:].strip())
    mult = 1 if dir == 'R' else -1
    dial += mult * amt
    div = dial // limit
    dial = dial % limit
    temp_clicks = 0
    temp_clicks += 1 if dial == goal else 0
    # conditional weirdness - surely there's a more clever solution
    if div > 0 and mult == 1 and dial == goal: div -= 1
    if div < 0 and dial_start == goal: div += 1
    div = div * -1 if div < 0 else div
    temp_clicks += div
    clicks += temp_clicks
print(clicks)

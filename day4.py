# Day 4-1
with open('files/4-1-input.txt') as file:
    rawlines = file.readlines()
# clean whitespace and convert to matrix
rawlines = [line.strip() for line in rawlines]
lines = []
for line in rawlines:
    t = []
    for ch in line:
        t.append(ch)
    lines.append(t)
limit = 4
valid = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '.':
            continue
        adj = 0
        mods = [-1, 0, 1]
        for y_mod in mods:
            y_check = y+y_mod
            # y out of bounds
            if y_check < 0 or y_check >= len(lines):
                continue
            for x_mod in mods:
                x_check = x+x_mod
                # check is current/center
                if y_mod == 0 and x_mod == 0:
                    continue
                # x out of bounds
                if x_check < 0 or x_check >= len(lines[y]):
                    continue
                if lines[y_check][x_check] == '@':
                    adj += 1
                    if adj == limit:
                        break
        if adj < limit:
            valid += 1
print(valid)


# Day 4-2
cleaned_lines = [line for line in lines]
limit = 4
valid = 0
y = 0
iterations = 0
while y < len(cleaned_lines):
    changed = False
    for x in range(len(cleaned_lines[y])):
        if cleaned_lines[y][x] == '.':
            continue
        adj = 0
        mods = [-1, 0, 1]
        for y_mod in mods:
            y_check = y+y_mod
            # y out of bounds
            if y_check < 0 or y_check >= len(cleaned_lines):
                continue
            for x_mod in mods:
                x_check = x+x_mod
                # check is current/center
                if y_mod == 0 and x_mod == 0:
                    continue
                # x out of bounds
                if x_check < 0 or x_check >= len(cleaned_lines[y]):
                    continue
                if cleaned_lines[y_check][x_check] == '@':
                    adj += 1
                    if adj == limit:
                        break
        if adj < limit:
            valid += 1
            cleaned_lines[y][x] = '.'
            changed = True
    if changed and y > 0:
        y -= 1
    else:
        y += 1
    iterations += 1
print(valid)
print(len(cleaned_lines),iterations)

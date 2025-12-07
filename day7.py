# Day 7-1
with open('files/7-1-input.txt') as file:
    lines = file.readlines()
splits = 0
beams = set()
for line in lines:
    if line.strip() =='':
        continue
    if len(beams) == 0:
        beams.add(line.find('S'))
        continue
    beams_to_remove = []
    beams_to_add = []
    for beam in beams:
        check = line[beam]
        if check == '^':
            splits += 1
            beams_to_remove.append(beam)
            beams_to_add.append(beam+1)
            beams_to_add.append(beam-1)
    for beam in beams_to_remove:
        beams.discard(beam)
    beams.update(beams_to_add)
print(splits)

# Day 7-2
beams = {}
splits = 0
for line in lines:
    if line.strip() =='':
        continue
    if len(beams) == 0:
        beams[(line.find('S'))] = 1
        continue
    check_beams = beams.copy()
    for beam in check_beams:
        if check_beams[beam] == 0:
            continue
        check = line[beam]
        if check == '^':
            pre = beam-1
            post = beam+1
            if pre not in beams:
                beams[pre] = 0
            if post not in beams:
                beams[post] = 0
            beams[pre] += beams[beam]
            beams[post] += beams[beam]
            beams[beam] = 0
for beam in beams:
    splits += beams[beam]
print(splits)

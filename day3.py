# Day 3-1
with open('files/3-1-input.txt') as file:
    lines = file.readlines()
pow_sum = 0
for line in lines:
    line = line.strip()
    l_hi = 0
    r_hi = 0
    for i in range(len(line)):
        p = int(line[i])
        if p > l_hi and i < len(line)-1:
            l_hi = p
            r_hi = 0
            continue
        if p > r_hi:
            r_hi = p
    pow_sum += r_hi + (10*l_hi)
print(pow_sum)

# Day 3-2
hi_len = 12
pow_sum = 0
for line in lines:
    line = line.strip()
    his = []
    for _ in range(hi_len): his.append(0)
    line_len = len(line)
    for i in range(line_len):
        p = int(line[i])
        for h in range(hi_len):
            if p > his[h] and i < line_len - (hi_len-h-1):
                his[h] = p
                for x in range(h+1, hi_len): his[x] = 0
                break
    histr = ''
    for h in his: histr = f'{histr}{h}'
    pow_sum += int(histr)
print(pow_sum)

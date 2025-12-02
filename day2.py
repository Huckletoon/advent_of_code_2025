# Day 2-1
with open('files/2-1-input.txt') as file:
    filedata = file.read()
ranges = filedata.strip().split(',')

id_sum = 0
for r in ranges:
    edges = r.split('-')
    start = edges[0]
    end = edges[1]
    if len(start) % 2 == 0:
        start_half = start[0:int(len(start)/2)]
    else:
        start_half = 10**int(len(start)//2)
    if len(end) % 2 == 0:
        end_half = end[0:int(len(end)/2)]
    else:
        end_half = 10**int(len(end)//2)
    for i in range(int(start_half),int(end_half)+1):
        check = int(f'{i}{i}')
        if check >= int(start) and check <= int(end):
            id_sum += check
print(id_sum)

# Day 2-1
id_sum = 0
for r in ranges:
    edges = r.split('-')
    start = edges[0]
    end = edges[1]
    lens = set()
    breaks = {}
    all_breaks = set()
    for l in range(len(start),len(end)+1):
        lens.add(l)
    for l in lens:
        if l not in breaks:
            breaks[l] = set()
        for i in range(1,l//2+1):
            if l % i == 0: 
                breaks[l].add(i)
                all_breaks.add(i)
    checked_ids = set()
    for l in breaks:
        for b in breaks[l]:
            start_edge = start[0:b]
            end_edge = end[0:b]
            if len(end) > l:
                end_edge = ['9' for _ in range(b)]
                end_edge = ''.join(end_edge)
            if len(start) < l:
                for i in range(b):
                    start_edge = '1' if i == 0 else f'{start_edge}0'
            reps = l/b
            for chunk in range(int(start_edge),int(end_edge)+1):
                check = ''
                for i in range(int(reps)):
                    check = f'{check}{chunk}'
                if check in checked_ids:
                    continue
                if int(check) >= int(start) and int(check) <= int(end):
                    id_sum+=int(check)
                checked_ids.add(check)
print(id_sum)

# Day 5-1
with open('files/5-1-input.txt') as file:
    lines = file.readlines()
ranges = []
range_starts = []
range_ends = []
fresh = 0
at_ing = False
# Collect ranges and ingredients
for line in lines:
    l = line.strip()
    if l == '' and not at_ing:
        at_ing = True
        continue
    if not at_ing:
        edges = l.split('-')
        s = int(edges[0])
        e = int(edges[1])
        merge_start = -1
        merge_end = -1
        for i in range(len(ranges)):
            if s <= range_ends[i] and s >= range_starts[i] and merge_start < 0:
                merge_start = i
            if e >= range_starts[i] and e <= range_ends[i] and merge_end < 0:
                merge_end = i
        # Merge ranges if needed
        if merge_start >= 0 and merge_end >= 0:
            ranges[merge_start] = f'{range_starts[merge_start]}-{range_ends[merge_end]}'
            range_ends[merge_start] = range_ends[merge_end]
            if merge_start != merge_end:
                ranges.pop(merge_end)
                range_starts.pop(merge_end)
                range_ends.pop(merge_end)
        elif merge_start >= 0:
            ranges[merge_start] = f'{range_starts[merge_start]}-{e}'
            range_ends[merge_start] = e
        elif merge_end >= 0:
            ranges[merge_end] = f'{s}-{range_ends[merge_end]}'
            range_starts[merge_end] = s
        else:
            ranges.append(l)
            range_starts.append(s)
            range_ends.append(e)
        continue
    # Check ingredients
    ing = int(l)
    for i in range(len(ranges)):
        if ing >= range_starts[i] and ing <= range_ends[i]:
            fresh += 1
            break
print(fresh)

# Day 5-2
valids = 0
for i in range(len(ranges)):
    valids += (range_ends[i]-range_starts[i]) + 1
print(valids)

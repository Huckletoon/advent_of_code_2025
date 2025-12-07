# Day 6-1
with open('files/6-1-input.txt') as file:
    lines = file.readlines()
cols = []
ops = []
sum = 0
for line in lines:
    nums = line.strip().split()
    if not nums:
        continue
    if nums[0].isdigit():
        for i in range(len(nums)):
            if len(cols) == i:
                cols.append([])
            cols[i].append(nums[i])
    elif nums[0] in ['+','*']:
        for op in nums:
            ops.append(op)
for i in range(len(cols)):
    temp = -1
    if ops[i] == '+':
        for num in cols[i]:
            if temp == -1:
                temp = int(num)
                continue
            temp += int(num)
    elif ops[i] == '*':
        for num in cols[i]:
            if temp == -1:
                temp = int(num)
                continue
            temp *= int(num)
    sum += temp
print(sum)

# Day 6-2
cols = []
big_iter = 0
op_row_index = -1
for i in range(len(lines)):
    if '+' in lines[i]:
        op_row_index=i
        break
sum = 0
for ch_iter in range(len(lines[0])):
    if len(cols) == big_iter:
        cols.append([])
    num = ''
    for row in lines[:op_row_index]:
        num = f'{num}{row[ch_iter]}'
    if num.strip() == '':
        big_iter += 1
        continue
    cols[big_iter].append(int(num))
for i in range(len(cols)):
    temp = -1
    if ops[i] == '+':
        for num in cols[i]:
            if temp == -1:
                temp = int(num)
                continue
            temp += int(num)
    elif ops[i] == '*':
        for num in cols[i]:
            if temp == -1:
                temp = int(num)
                continue
            temp *= int(num)
    sum += temp
print(sum)

length = int(input())
nums = list(map(int, input().split(" ")))
bit_score = []
occ_odd = [0]*10
occ_even = [0]*10
counts = [0]*10

def largest(num):
    num_str = str(num)
    i = 9
    while i >= 0:
        if str(i) in num_str:
            return i
        i -= 1

def smallest(num):
    num_str = str(num)
    i = 0
    while i <= 9:
        if str(i) in num_str:
            return i
        i += 1

def pairs(num):
    if num == 0:
        return 1
    if num >= 3:
        return 2
    return 0

for i in length:
    l = largest(i)
    s = smallest(i)
    val = str((11*l) + (7*s))
    if len(val) > 2:
        val = val[-2:]
    bit_score.append(val)

for i in range(len(bit_score)):
    msd = int(bit_score[i][0])
    if i % 2 == 0:
        occ_even[msd] += 1
    else:
        occ_odd += 1

for i in range(10):
    if (occ_even[i] <= 1 and occ_odd[i] <= 1):
        continue
        
    count[i] += int(pairs(occ_even[i]) + pairs(occ_odd[i]))
    count[i] = min(2, count[i])

print(sum(count))
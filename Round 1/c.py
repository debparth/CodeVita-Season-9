nt = int(input())
arr_list = []
dep_list= []

for i in range(0, nt):
    temp1, temp2 = input().split(' ')
    arr_list.append(int(temp1))
    dep_list.append(int(temp2))

for i in range(0, nt):
    dep_list[i] = arr_list[i] + dep_list[i]

def count(arr_list, dep_list, n):
    platform = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n):
        if (arr_list[i] <= dep_list[j]):
            platform += 1
            i += 1
        else:
            platform -= 1
            j += 1
        if platform > result:
                result = platform

    return result

n = len(arr_list)
output = count(arr_list, dep_list, n)
print(output)
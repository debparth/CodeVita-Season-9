no = int(input())
i = 0
count_list = []

for i in range(0, no):
    emp = int(input())
    emp_rank_list = []
    max_rank = 1
    count = 0
    
    emp_rank_list.append(input().split(" "))
    emp_rank_list = [int(item) for sublist in emp_rank_list for item in sublist]

    for i in range(0, emp):
        if max_rank == emp_rank_list[i] or max_rank > emp_rank_list[i]:
            count += 1
        else:
            count += 2
            max_rank = emp_rank_list[i]

    count_list.append(count)

for i in count_list:
    print(i)
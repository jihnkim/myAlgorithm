array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1]]

answer = []
for v in commands:
    i = v[0]
    j = v[1]
    k = v[2]

    lst = array
    lst = lst[i-1:j]
    lst.sort()
    answer.append(lst[k-1])

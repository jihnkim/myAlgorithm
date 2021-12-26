"""
1546
"""

num = int(input())
lst = list(map(int, input().split()))

lst.sort()

n_lst = [(x / lst[-1]) * 100 for x in lst]

print(sum(n_lst) / num)
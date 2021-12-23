"""
2562
"""

arr = []
for loc in range(1, 10):
    arr.append([int(input()), loc])

def solution(arr):
    arr.sort()
    print(arr[-1][0], arr[-1][1])

solution(arr)
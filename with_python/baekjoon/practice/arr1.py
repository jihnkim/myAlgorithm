"""
10818
"""

N = int(input())
arr = list(map(int, input().split()))

def solution(arr):
    arr.sort()
    print(arr[0], arr[-1])

solution(arr)
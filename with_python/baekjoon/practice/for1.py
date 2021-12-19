num = int(input())

def solution(num):
    for i in range(1, num + 1):
        print(" " * (num - i) + i * '*')

solution(num)
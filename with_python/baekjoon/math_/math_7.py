n = int(input())

def solution(n):
    d = (n % 5)
    m = 0
    cnt = 0
    while True:
        if d > n:
            return -1
        cnt += (n // 5) + (d // 3)
        if (d % 3) != 0:
            d += 5
            m -= 1
            cnt = m
        else:
            break
    
    return cnt


print(solution(n))
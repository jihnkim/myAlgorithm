"""
11653
소인수 분해

첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.  

N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
"""

# 시간초과 NlogN 으로 해보자
def isPrime(n):
    if n == 1:
        return 0
    
    for i in range(2, n):
        if n % i == 0:
            return 0
    
    return 1

N = int(input())
lst = [i for i in range(1, N + 1) if isPrime(i)]
idx = 0

while True:
    if N == 1:
        break

    if N % lst[idx] == 0:
        N = (N // lst[idx])
        print(lst[idx])
        continue
    
    idx += 1



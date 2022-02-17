"""
1929
소수 구하기

문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""

# import math

# M, N = map(int, input().split())
    
# div = 2
# while M <= N:
#     if (M % div == 0) or (div > M):
#         if M == 2:
#             print(M)
#         div = 2
#         M += 1
#         continue

#     if (div > math.sqrt(M)):
#         print(M)
#         div = 2
#         M += 1
#         continue

#     div += 1

M, N = map(int, input().split())

def isPrime(n):
    if n == 1:
        return 0
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
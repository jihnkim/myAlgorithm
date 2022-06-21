n = int(input())

def isPrime(n):
    if n == 1:
        return 0
    
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if isPrime(i):
            answer += 1

    return answer

print(solution(n))
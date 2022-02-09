"""
2581
소수

자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 

이들 소수의 합은 620이고, 최솟값은 61이 된다.

"""
def isPrime(n):
    if n == 1:
        return 0
    
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def isEmpty(lst):
    if len(lst):
        return 0
    return 1

res = [i for i in range(int(input()), int(input()) + 1) if isPrime(i)]

if isEmpty(res):
    print(-1)

else:
    print(sum(res))
    print(res[0])

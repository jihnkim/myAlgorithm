"""
1978

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
"""

N = int(input())

for i in map(int, input().split(" ")):
    if i == 1:
        N -= 1
        continue

    for num in range(2, i):
        if i % num == 0:
            N -= 1
            break
        
print(N)
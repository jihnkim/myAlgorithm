"""
11653
소인수 분해

첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.  

N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
"""

N = int(input())
div = 2

# main logic
while div <= N:
    # can factorize?
    if N % div == 0:
        print(div)
        N = N / div
        continue

    div += 1

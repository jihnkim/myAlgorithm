"""
11659
구간 합

문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
"""

# 1트 시간초과 다른방법이 있는듯

# n ,cnt = map(int, input().split(' '))

# lst = list(map(int, input().split()))

# for i in range(cnt):
#     st, ed = map(int, input().split(' '))
#     print(sum(lst[st - 1:ed]))


# 배열에 값을 저장한 후 인덱스 부터 하나씩 더하는 경우 최악의 경우 n^2
# prefix sum 방식을 이용 > N으로 해결가능
import sys
n ,cnt = map(int, sys.stdin.readline().split(' '))

arr = [0]
sn = 0

for v in list(map(int, sys.stdin.readline().split(' '))):
    sn += v
    arr.append(sn)

for i in range(cnt):
    st, ed = map(int, sys.stdin.readline().split(' '))
    print(arr[ed] - arr[st-1])
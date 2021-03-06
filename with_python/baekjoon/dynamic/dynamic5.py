"""
1149
RGB 거리

문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
"""

n_house = int(input())

lst = [list(map(int, input().split())) for _ in range(n_house)]

for i in range(1, n_house):
    # lst[i][0]이 의미하는 것은 i 번째 집에 빨강칠을 했을 때 비용
    # dp - 값을 저장하며 나아간다를 기억하자.
    lst[i][0] = min(lst[i - 1][1], lst[i - 1][2]) + lst[i][0]

    # 마찬가지로 초록칠 했을 때 비용
    lst[i][1] = min(lst[i - 1][0], lst[i - 1][2]) + lst[i][1]

    # 파랑칠 비용
    lst[i][2] = min(lst[i - 1][0], lst[i - 1][1]) + lst[i][2]

# 그럼 최종적으로 [...[minConst1, minConst2, minConst3]] 요런 리스트가 되는데
# 마지막 요소의 최솟값을 출력해 주면 됨
print(min(lst[-1]))

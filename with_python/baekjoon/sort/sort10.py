"""
18870
좌표 압축

문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109
"""

# 1트 시간 초과
import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split(' ')))

unique_lst = list(set(lst))
unique_lst.sort()

# 여기서 O(MN)이라 안되는 듯
for v in lst:
    print(unique_lst.index(v), end=' ')

# 2트
import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split(' ')))

unique_lst = list(set(lst))
unique_lst.sort()

tmp = {unique_lst[idx] : idx for idx in range(len(unique_lst))}

for v in lst:
    print(tmp[v], end=' ')

"""
2751
수 정렬 2

문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


## tip

파이썬에서 입력을 받을 때 sys.stdin.readline()사용?

*
input -> 개행문자를 벗겨 내어 -> 문자열로 변환 -> return
의 절차를 거친다.

**
내장함수인 input()과 달리 sys.stdin은 file object이다.
사용자의 입력을 받는 buffer를 만들어 그 buffer에서 읽어들이는 것이다.
단, 개행문자도 같이 입력되기 때문에 rstrip()이나 int() 등으로 개행 제거 필요

***
merge sort 를 사용하여 복잡도를 개선하는 방법도 있음
"""

import sys

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

for v in sorted(lst):
    print(v)
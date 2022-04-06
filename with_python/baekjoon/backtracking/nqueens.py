"""
9663

N-Queens

진짜 개어려웠따

문제
N-Queen 문제는 크기가 N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

##################################################
기본적으로 1차원 리스트 하나를 이용하여 트리를 구현할 경우,
인덱스를 행, 값을 열로 간주하고 접근.
이후 완전탐색을하며 순회를 하는데 유망한지 여부도 판단

4 * 4를 예로 들어서 설명
N_queen(row=0)

lst[row=0]=0, check=True, N_queen(row=1) 재귀함수 작동
    lst[row=1]=0, check=False(lst[row=0]과 같음), 다음 열로 넘어감
    lst[row=1]=1, check=False(lst[row=0]의 남동쪽 대각선에 포함), 다음 열로 넘어감
    lst[row=1]=2, check=True, N_queen(row=2) 재귀함수 작동
        lst[row=2]=0, check=False(lst[0]과 같음), 다음열로 넘어감
        lst[row=2]=1, check=False(lst[1]의 남서쪽 대각선에 포함), 다음열로 넘어감
        check=False(lst[1]과 같음), 다음열로 넘어감
        check=False(lst[1]의 남동쪽 대각선에 포함), 다음열로 넘어감
        row=2에서의 for문을 모두 거쳤음에도 불구하고 재귀함수를 동작하지 못했으므로 count=0인 상태로 반환
    lst[row=1]=3, check=True, N_queen(row=2)재귀함수 작동
        lst[row=2]=0, check=False
        lst[row=2]=1, check=True, N_queen(row=3) 재귀함수 작동
            lst[row=3]=0, 다음열 넘어감
            lst[row=3]=1, 다음열
            lst[row=3]=2, 다음열
            lst[row=3]=3 다음열
            row=3에서의 for문을 모두 거쳤음에도 불구하고 재귀함수 동작 못했으므로 count=0으로 반환
        lst[row=2]=2, 다음열
        lst[row=2]=3, 다음열
        row=2에서 for문 거쳤음에도 불구하고 재귀함수 동작 못했으므로 count=0반환
    row=1에서 for문ㅇ 거쳤음에도 불구하고 재귀함수 동작x, count=0반환
lst[row=0]=1,check=True, N_queen(row=1) 재귀함수 작동
"""

n = int(input())

cnt = 0
row = [0] * n

def isPromising(x):
    for i in range(x):
        # 1. 같은 열에 다른 퀸이 있는 지 체크
        # 2. 대각선(왼쪽과 오른쪽 대각선)에 다른 퀸이 있는 지 체크
        # (1, 1)에 퀸이 있을 때 (2, 2), (3, 3)이 대각선인데
        # 1 - 2 == 1 - 2, 1 - 3 == 1 -3 이고
        # (0, 2)일때도 마찬가지로
        # abs(1 - 0) == abs(1 - 2) 임 
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global cnt
    if x == n: # 다 돌았는데 이상없으면 1 추가
        cnt += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if isPromising(x): # 유망한가? 그렇다면 다음 행에 퀸을 놓으러 가자
                n_queens(x+1) # 다음행에 퀸놓고 재귀시작

n_queens(0)
print(cnt)
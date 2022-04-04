"""
15649
N과 M 1

문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

*****************************************************
back tracking?
>> 완전검색후 가지치기를 한 것 즉, 불필요한 계산낭비를 방지하는 방법
>> 재귀로 풀 수 있다.

"""
def backtracing(depth, N, M):
    # depth는 원하는 해(값)이 아니면 그 다음 노드를 탐색(깊이 우선)
    # 탈출조건
    if depth == M:
        print(' '.join(map(str, out)))
        return
    
    # N 만큼 탐색 시작
    for i in range(N):
        # 만약 검색하지 않은 값이라면?
        if not visit[i]:
            visit[i] = 1 # 탐사를 했다고 표시 하고
            out.append(i + 1) # 결과 리스트에 1 추가
            print('DEPTH :', depth + 1, 'INDEX :', i)
            backtracing(depth + 1, N, M) # 그 후 다음 해를 찾아봄
            visit[i] = 0 # 탐사가 끝났음을 표시 하고
            out.pop() # 탐사 내용을 없애줌 (다음 탐사를 위해)

if __name__ == '__main__':
    N, M = map(int, input().split())
    # 리스트 최대길이 = N 값
    visit = [0] * N
    out = []

    backtracing(0, N, M)
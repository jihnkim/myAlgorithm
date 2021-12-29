"""
4344
문자열 포매팅 시 자릿수 제한법
> f'{VALUE:.2f}' 중괄호안의 값을 두자리까지만 출력
> round는 특정 자리수를 전부 뽑아내지는 못함
"""

N = int(input())

for _ in range(N):
    score_lst = list(map(int, input().split()))[1:]
    n = len(score_lst)
    avg = sum(score_lst) / n

    cnt = 0
    for score in score_lst:
        if score - avg > 0: cnt += 1
    
    print(f'{round((cnt / n) * 100, 3):.3f}%')
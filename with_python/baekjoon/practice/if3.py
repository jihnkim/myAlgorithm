H, M = map(int, input.split())

def solution(H, M):
    tmp = M - 45
    if tmp < 0:
        if not H:
            return print(23, 60 + tmp)
        return print(H - 1, 60 + tmp)
    print(H, M - 45)

solution(H, M)
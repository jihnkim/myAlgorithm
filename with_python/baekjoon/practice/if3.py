H, M = input().split()
H, M = int(H), int(M)

def solution(H, M):
    tmp = M - 45
    if tmp < 0:
        if not H:
            return print(23, 60 + tmp)
        else:
            return print(H - 1, 60 + tmp)
    print(H, M - 45)

solution(H, M)
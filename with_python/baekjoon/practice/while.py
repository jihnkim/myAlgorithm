"""
1110
"""
N = input()

def solution(N):
    cnt = 0
    while True:
        if len(N) < 2: N = f'0{N}' 
        if not cnt: M = N
        N = N[-1] + str(int(N[0])+ int(N[-1]))[-1]
        cnt += 1
        if M == N: return cnt

print(solution(N))
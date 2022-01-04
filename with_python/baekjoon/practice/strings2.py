"""
11720

숫자의 합
"""

N = int(input())
sent = input()
S = 0
for i in range(N):
    S += int(sent[i])

print(S)
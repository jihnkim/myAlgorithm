"""
8958
"""

N = int(input())

score, cnt = 0, 0

for _ in range(N):
    sent = input() # OOXXOXXOOO
    for spell in sent:
        if spell == "O":
            cnt += 1
            score += cnt
            continue
        cnt = 0
    print(score)
    score, cnt = 0, 0
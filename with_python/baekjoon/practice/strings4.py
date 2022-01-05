"""
2675
문자열 반복
줄 바꿈시 그냥 상위 반복문에 print() 넣는 방법도 있다.
"""

T = int(input())

for _ in range(T):
    s = input()
    i, S = int(s[:1]), s[2:]
    for spell in S:
        print(spell * i, end='')
    print()
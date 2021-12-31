"""
4673

셀프 넘버 찾기

n 은 10000 이하의 양의 정수
"""

def d(n):
    return n + sum(map(int, str(n)))

lst = [d(x) for x in range(1, 10000)]

for i in range(1, 10000):
    if i not in lst:
        print(i)
"""
2869

달팽이는 올라가고싶다.

땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

a 는 올라가는 m
b 는 잠을자는동안 내려가는 m
v 는 총 나무의 길이
"""

def solution(a, b, v):
    # 기존 나무의 길이 에서 내려가는 길이를 미리 빼준다
    # 그러면 편하게 계산 가능 
    d = (v - b) / (a - b)
    if (v - b) % (a - b) != 0:
        return int(d + 1)
    return int(d)

a, b, v = map(int, input().split())
print(solution(a, b, v))
"""
1316

그룹 단어 체커
"""

lst = [input() for _ in range(int(input()))]
cnt = len(lst)

for w in lst:
    s = ''.join(sorted(w))
    for l in w:
        if (w.rfind(l) - w.find(l)) != (s.rfind(l) - s.find(l)):
            cnt -= 1
            break

print(cnt)
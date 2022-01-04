"""
10809

알파벳 찾기
list to str > ' '.join(list) "if want space"
"""
S = input()
targets = [chr(x) for x in range(97, 123)]
res = []

for target in targets:
    if target not in S:
        res.append('-1')
        continue
    res.append(str(S.index(target)))

print(' '.join(res))
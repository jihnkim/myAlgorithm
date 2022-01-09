"""
** 다시 풀어보자
5622

다이얼 문제
음,, 뭔가 색다른 풀이가 없을까요
다중 for loop 맘에 안듦 (단어 길이가 길어지거나 리스트가 무한이라면 ? -> O(MN))
"""

lst = ['', '', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

t = 0
for l in input().lower():
    for w in lst:
        if l in w:
            t += lst.index(w)
print(t)
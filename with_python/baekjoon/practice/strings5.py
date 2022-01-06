"""
1157

가장많이 존재하는 알파벳 대문자 출력(중복시 ? 출력)

>> 소문자 string.lower()
>> 집합 컴프리헨션도 가능
"""

s = input().lower()
lst = list({x for x in s})
res = [[s.count(l), l] for l in lst]

res.sort()

if len(res) > 1:
    if res[-1][0] == res[-2][0]:
        print('?')
    else:
        print(res[-1][1].upper())
else:
    print(res[-1][1].upper())
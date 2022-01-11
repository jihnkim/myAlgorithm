"""
2908

check this out 나는 정 "상수"
우리 상수는 수를 거꾸로 읽는 다네요 
상수입장에서 대소비교를 해봅시다

sort는 return 값이 없음
"""

lst = [int(x[::-1]) for x in input().split(" ")]
lst.sort()

print(lst[-1])
"""
3052

tip 리스트의 유니크한 값을 나타 낼 때 set 자료형으로 바꾸는 것도 있음
"""
lst = []
cnt = 0
for i in range(10):
    num = int(input()) % 42
    if num not in lst: cnt += 1
    lst.append(num)

print(cnt)
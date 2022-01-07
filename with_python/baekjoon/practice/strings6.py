"""
1152

단어의 개수
>> string.split() 하면 공백이 사라진다
"""
# 1
print(len(input().split()))

# 2
lst = input().split(" ")

if lst[0] == '':
    lst = lst[1:]

if lst[-1] == '':
    lst = lst[:-1]

print(len(lst))
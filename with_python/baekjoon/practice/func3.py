"""
1065

한수란? 
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 

N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
"""

N = int(input())

cnt = 0
for i in range(1, N + 1):
    lst = list(map(int, str(i))) # 123 [1, 2, 3]
    if len(lst) > 2:
        if (lst[1] - lst[0]) == (lst[2] - lst[1]):
            cnt += 1
        continue
    cnt += 1

print(cnt)  

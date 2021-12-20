N, X = map(int, input().split())
A = list(map(int, input().split()))

# def solution(X, A):
#     _ = [print(num, " ", end='') for num in A if num < X]

# solution(X, A)

lst = []
for num in A:
    if num < X:
       lst.append(num)

A = " ".join(map(str, lst))
print(A)
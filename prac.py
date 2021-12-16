import numpy as np

from kakao2 import rotate


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
lock2 = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [1, 1, 1, 1]]

# answer = True
# for i in range(len(lock)):
#     for j in range(len(lock)):
#         if lock[i][j] != 1:
#             answer = False
#             break
    
# print(answer)

new_key = []
for i in zip(*key):
    new_key.append(list(i[::-1]))

new_key = key
def rotate(key):
    tmp = []
    for i in zip(*key):
        tmp.append(list(i[::-1]))

    return tmp

for i in range(4):
    new_key = rotate(new_key)
    print(new_key)
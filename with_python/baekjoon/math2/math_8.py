"""
3009
네 번째 점

축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
"""
lstx = []
lsty = []
for _ in range(3):
    x, y = map(int, input().split(' '))
    lstx.append(x)
    lsty.append(y)
lstx.sort()
lsty.sort()
if lstx[1] == lstx[0]:
    x = lstx[2]
else:
    x = lstx[0]

if lsty[1] == lsty[0]:
    y = lsty[2]
else:
    y = lsty[0]

print(x, y)
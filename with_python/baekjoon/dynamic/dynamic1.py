
"""
1003
피보나치 함수

문제
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
"""

"""
DP 동적계획법 팁

- 일반적인 재귀를 이용하면 값이 중복되어 호출되기 때문에 사용 x

한번 구한 수는, 다시 구하지 않고 값을 저장하여 이용할 수 있도록
DP(Dynamic Programming)개념을 이용하면 된다.

d라는 리스트를 2차원으로 만들어 d[x][0]에는 0이 호출된 횟수, d[x][1]에는 1이 호출된 횟수를 저장하였다.
0일 경우는 1, 0

1일 경우는 0,1 이 고정이므로 이 두개 값만 고정값으로 두고

3부터는 이전의 값을 이용해 구하도록 구현
"""

t = int(input())

for i in range(t):
    n = int(input())

    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")

    else:
        d = [[0] * 2 for _ in range(n + 1)]
        d[0][0] = 1
        d[1][1] = 1
        d[2] = [1, 1]
        for j in range(3, n + 1):
            d[j][0] = d[j - 1][0] + d[j - 2][0]
            d[j][1] = d[j - 1][1] + d[j - 2][1]

        print("%d %d" % (d[n][0], d[n][1]))


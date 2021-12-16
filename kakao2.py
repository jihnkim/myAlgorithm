
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]] -> key
# [[1, 1, 1], [1, 1, 0], [1, 0, 1]] -> lock

def solution(key, lock):
    M = len(key)
    N = len(lock)

    # padding 된 새로운 자물쇠 생성
    new_lock = mk_new_lock(M, N, lock)
    # print(new_lock)

    new_key = key
    for iter in range(4):
        new_key = rotate(new_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                joined_lock = join(new_lock, new_key, M, x, y)
                if is_correct(M, N, joined_lock):
                    return True
                joined_lock = remove(joined_lock, new_key, M, x, y)

    return False

def mk_new_lock(M, N, lock):
    new_lock = []
    # key 길이 만큼 양 옆에 0 추가
    for i in range(M*2 + N):
        new_lock.append([0] * (M*2 + N))

    # M 부터 시작하는 위치에 기존 자물쇠 삽입
    for i in range(N):
        for j in range(N):
            new_lock[M+i][M+j] = lock[i][j]

    return new_lock

def join(new_lock, key, M, x, y):
    for i in range(M):
        for j in range(M):
            new_lock[x+i][y+j] += key[i][j]

    return new_lock

def remove(new_lock, key, M, x, y):
    for i in range(M):
        for j in range(M):
            new_lock[x+i][y+j] -= key[i][j]

    return new_lock

def rotate(key):
    tmp = []
    for i in zip(*key):
        tmp.append(list(i[::-1]))

    return tmp

def is_correct(M, N, joined_lock):
    # key를 이동해서 넣었을 때 맞는 지 확인
    for i in range(N):
        for j in range(N):
            if joined_lock[M+i][M+j] != 1:
                return False
    return True

if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
def solution(p):
    answer = ''

    if p == '' or is_okay(p):
        return p

    u, v = str_split(p)
    # print(u, v)

    if is_okay(u):
        answer = u + solution(v)

    else:
        answer = '(' + solution(v) + ')'

        # 괄호 방향 뒤집기
        for spell in u[1:len(u)- 1]:
            if spell =='(':
                answer += ')'
            else:
                answer += '('

    return answer

# 균형 잡힌 u, v로 분리
def str_split(p):
    u, v = '', ''
    idx_1 = 0
    idx_2 = 0

    for i in range(1, len(p) + 1):
        if p[i - 1] == '(':
            idx_1 += 1

        else:
            idx_2 += 1

        if idx_1 == idx_2:
            u = p[:i]
            if i < len(p):
                v = p[i:]
            else:
                v = ''
            break
    return u, v

# 올바른 괄호 문자열인지 체크
def is_okay(u):
    tmp_lst = []
    for spell in u:
        if spell == '(':
            tmp_lst.append(spell)

        else:
            if not tmp_lst:
                return False
            elif tmp_lst[-1] == '(':
                tmp_lst = tmp_lst[:-1]
    
    if tmp_lst:
        return False
    else:
        return True




if __name__ == '__main__':
    print(solution('()))((()'))
    # solution('()))((()')
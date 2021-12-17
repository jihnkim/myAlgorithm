# y = 2000

def solution(y):
    if not y % 4:
        if y % 100:
            return 1
        else:
            if not y % 400:
                return 1
            else:
                return 0
        
    return 0

print(solution(2400))

# 완전 탐색
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
result_lst = []

def find_wild(query):
    wild_cnt = query.count("?")
    if query[0] == '?':
        return 1, wild_cnt
    
    else:
        return 0, wild_cnt

def is_match(word, query, is_front, wild_cnt):
    if len(word) == wild_cnt:
        return True

    if is_front:
        if word[wild_cnt:] == query[wild_cnt:]:
            return True
    else:
        if word[:-wild_cnt] == query[:-wild_cnt]:
            return True

def solution(words, queries):
    result_lst = []
    match_cnt = 0
    for query in queries:
        is_front, wild_cnt = find_wild(query)
        for word in words:
            if is_match(word, query, is_front, wild_cnt):
                match_cnt += 1

        result_lst.append(match_cnt)
        match_cnt = 0
    return result_lst
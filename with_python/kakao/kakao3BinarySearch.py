
# 가사 검색 동일 문제 다른 해법 
# 복잡도 개선(기존MN) -> 이분탐색

queries = ["fro??", "????o", "fr???", "fro???", "pro??"]
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]


def solution(words, queries):
    result_lst = []

    # 이 후 탐색을 위한 sorting
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    reversed_words.sort()
    words.sort()

    # 문자열의 길이 분류
    reversed_word_dic = make_dict(reversed_words)
    word_dic = make_dict(words)
    # print(reversed_word_dic, word_dic)

    # matching
    for query in queries:
        if query[0] == '?':
            if len(query) not in reversed_word_dic:
                return result_lst.append(0)
            else:
                reverse_query = query[::-1]
                lst = reversed_word_dic[len(query)]
                right_input = reverse_query.replace('?', 'z')
                left_input = reverse_query.replace('?', 'a')
                cnt = right_search(lst, right_input) - left_search(lst, left_input)
                result_lst.append(cnt)
        
        else:
            if len(query) not in word_dic:
                return result_lst.append(0)
            else:
                lst = word_dic[len(query)]
                right_input = query.replace('?', 'z')
                left_input = query.replace('?', 'a')
                cnt = right_search(lst, right_input) - left_search(lst, left_input)
                result_lst.append(cnt)

    return result_lst

def right_search(lst, target):
    low = 0
    high = len(lst)
    while low < high: # target -> frozz, ozzzz
        mid = (low + high) // 2 # mid = 3, 5
        if target < lst[mid]:  
            high = mid
        else: 
            low = mid + 1
    return low

def left_search(lst, target):
    low = 0
    high = len(lst)
    while low < high: # target -> froaa ,oaaaa
        mid = (low + high) // 2 
        if lst[mid] < target: 
            low = mid + 1
        else: 
            high = mid
    return low

# dict 에 없는 요소는 추가하고, 존재할 경우 list에 추가
# collections.defaultdict package도 있긴 함
def make_dict(lst):
    dic = dict()
    for word in lst:
        if len(word) not in dic:
            dic[len(word)] = [word]
            continue
        dic[len(word)].append(word)
    return dic

if __name__ == '__main__':
    print(solution(words, queries))

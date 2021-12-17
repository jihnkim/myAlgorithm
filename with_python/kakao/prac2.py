queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
result_lst = []

# print("frodo"[::-1])

# default dict make
from collections import defaultdict
from bisect import bisect_left, bisect_right

# wild_front_dict = defaultdict(list)
# wild_back_dict = defaultdict(list)

# for word in words:
#     wild_front_dict[len(word)].append(word)
#     wild_back_dict[len(word)].append(word[::-1])

####

reversed_words = []
for word in words:
    reversed_words.append(word[::-1])

reversed_words.sort()
words.sort()

print(reversed_words, words)

def right_search(lst, target):
    low = 0
    high = len(lst)
    while low < high: # target = frozz
        mid = (low + high) // 2 # mid = 3, 5
        if target < lst[mid]:  
            high = mid
        else: 
            low = mid + 1
    return low

def left_search(lst, target):
    low = 0
    high = len(lst)
    while low < high: # target -> froaa
        mid = (low + high) // 2 
        if lst[mid] < target: 
            low = mid + 1
        else: 
            high = mid
    return low

def make_dict(lst):
    dic = dict()
    for word in lst:
        if len(word) not in dic:
            dic[len(word)] = [word]
            continue
        dic[len(word)].append(word)
    return dic

print(make_dict(words))
# print(right_search(words, 'frozz'))
# print(left_search(words, 'froaa'))

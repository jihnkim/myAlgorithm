"""
2941

크로아티아 알파벳 개수
"""

lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()

for t in lst:
    w = w.replace(f'{t}',' ')

print(len(list(w)))
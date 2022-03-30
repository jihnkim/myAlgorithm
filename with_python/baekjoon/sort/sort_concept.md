### 정렬 알고리즘 정리 노트

1. 선택 정렬(Selection sort)

- 로직 설명
  
    ① 정렬 되지 않은 인덱스의 맨 앞에서 부터, 이를 포함한 그 이후의 배열값 중 가장 작은 값을 찾아간다.

    (정렬되지 않은 인덱스의 맨 앞은, 초기 입력에서는 배열의 시작위치일 것이다.)

    ② 가장 작은 값을 찾으면, 그 값을 현재 인덱스의 값과 바꿔준다.

    ③ 다음 인덱스에서 위 과정을 반복해준다.

- 시간 복잡도

    최선 최악 O(N^2)

- 로직 구현

```python
def selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
            	min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    print(arr)
```


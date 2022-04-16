### 정렬 알고리즘 정리 노트

#### 1. 선택 정렬(Selection sort)

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

- 구현 시각화

    ![selection_sort](https://user-images.githubusercontent.com/86646616/160958199-aab17db0-9f06-4b4c-bf7e-e84fe3695751.gif)

***

#### 2. 삽입 정렬(Insertion sort)

- 로직 설명
    
    ① 삽입 정렬은 두 번째 인덱스부터 시작한다. 현재 인덱스는 별도의 변수에 저장해주고, 비교 인덱스를 현재 인덱스 -1로 잡는다.

    ② 별도로 저장해 둔 삽입을 위한 변수와, 비교 인덱스의 배열 값을 비교한다. 

    ③ 삽입 변수의 값이 더 작으면 현재 인덱스로 비교 인덱스의 값을 저장해주고, 비교 인덱스를 -1하여 비교를 반복한다.

    ④ 만약 삽입 변수가 더 크면, 비교 인덱스+1에 삽입 변수를 저장한다.

- 시간 복잡도

    최선 O(N) - 정렬된 경우 1번만 비교하기 때문

    최악 O(N^2)

- 로직 구현

    ```python
    def insertion(arr):
        for i in range(1, len(arr):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break
        print(array)
    ```

- 구현 시각화

    ![insertion_sort](https://user-images.githubusercontent.com/86646616/160963112-cafe9092-a0f2-4624-93aa-69b24444aa7d.gif)

***

#### 3. 버블 정렬(Bubble sort)

- 로직 설명

    ① 버블 정렬은 두 번째 인덱스부터 시작한다. 현재 인덱스 값과, 바로 이전의 인덱스 값을 비교한다.

    ② 만약 이전 인덱스가 더 크면, 현재 인덱스와 바꿔준다. 

    ③ 현재 인덱스가 더 크면, 교환하지 않고 다음 두 연속된 배열값을 비교한다.

    ④ 이를 (전체 배열의 크기 - 현재까지 순환한 바퀴 수)만큼 반복한다.

- 시간 복잡도

    최선 최악 O(N^2)

- 로직 구현

    ```python
    def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
           if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
              
    print(arr)
    ```

- 구현 시각화

    ![bubble_sort](https://user-images.githubusercontent.com/86646616/160966181-8b0992dd-5def-43c0-a37c-8d03d534b6a1.gif)

***

#### 4. 합병 정렬(Merge sort)

- 로직 설명

    | divide

    ① 현재 배열을 반으로 쪼깬다. 배열의 시작 위치와, 종료 위치를 입력받아 둘을 더한 후 2를 나눠 그 위치를 기준으로 나눈다.

    ② 이를 쪼갠 배열의 크기가 0이거나 1일때 까지 반복한다. 

    | conquer

    ① 두 배열 A,B의 크기를 비교한다. 각각의 배열의 현재 인덱스를 i,j로 가정하자.

    ② i에는 A배열의 시작 인덱스를 저장하고, j에는 B배열의 시작 주소를 저장한다.

    ③ A[i]와 B[j]를 비교한다. 오름차순의 경우 이중에 작은 값을 새 배열 C에 저장한다. 

     A[i]가 더 컸다면 A[i]의 값을 배열 C에 저장해주고, i의 값을 하나 증가시켜준다.

    ④ 이를 i나 j 둘중 하나가 각자 배열의 끝에 도달할 때 까지 반복한다.

    ⑤ 끝까지 저장을 못한 배열의 값을, 순서대로 전부 다 C에 저장한다.

    ⑥ C 배열을 원래의 배열에 저장해준다.


- 시간 복잡도

    최선 최악 O(NlogN)

- 로직 구현

     ```python
    def merge_sort(arr, l, r):
    if r > 1:
       mid = (l+r) // 2
       
       left = arr[:mid]
       right = arr[:mid]
       merge_sort(left, l, m-1)
       merge_sort(right, m, r)
       
       i = j = k = 0
       while i < len(left) and j < len(right):
           if left[i] < right[i]:
               arr[k] = left[i]
               i+=1
           else:
               arr[k] = right[j]
               j+=1
           k+=1
       while i < len(left):
           arr[k] = left[i]
           i+=1
           k+=1
       while j < len(right):
           arr[k] = right[j]
           j+=1
           k+=1
    ```

- 구현 시각화

    ![merge_sort](https://user-images.githubusercontent.com/86646616/160966927-9789bee4-4d85-4163-b9f8-9bcf684c9e42.gif)


### 5. 힙 정렬

***
##### REFERENCE

https://hsp1116.tistory.com/33
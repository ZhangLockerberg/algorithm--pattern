# 排序

## 常考排序

### 快速排序

```Python
def partition(A, start, end):
    if start >= end:
        return
    
    l, r = start, end - 1
    while l < r:
        while l < r and A[l] <= A[end]:
            l += 1
        while l < r and A[r] >= A[end]:
            r -= 1
        
        A[l], A[r] = A[r], A[l]
    
    swap = r + int(A[r] < A[end])

    A[end], A[swap] = A[swap], A[end]

    partition(A, swap + 1, end)
    partition(A, start, swap - 1)

    return

def quicksort(A):
    partition(A, 0, len(A) - 1)
    return A

if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(quicksort(a))
```

### 归并排序

```Python
def merge(A, B):
    C = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    if i < len(A):
        C += A[i:]
    
    if j < len(B):
        C += B[j:]
    
    return C

def mergsort(A):
    n = len(A)
    if n < 2:
        return A[:]
    
    left = mergsort(A[:n // 2])
    right = mergsort(A[n // 2:])

    return merge(left, right)

if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(mergsort(a))
```

### 堆排序

用数组表示的完美二叉树 complete binary tree

> 完美二叉树 VS 其他二叉树

![image.png](https://img.fuiboom.com/img/tree_type.png)

[动画展示](https://www.bilibili.com/video/av18980178/)

![image.png](https://img.fuiboom.com/img/heap.png)

核心代码

```Python
def heap_adjust(A, start=0, end=None):
    if end is None:
        end = len(A)
    
    while start is not None and start < end // 2:
        l, r = start * 2 + 1, start * 2 + 2
        swap = None

        if A[l] > A[start]:
            swap = l
        if r < end and A[r] > A[start] and (swap is None or A[r] > A[l]):
            swap = r

        if swap is not None:
            A[start], A[swap] = A[swap], A[start]
            
        start = swap
    
    return

def heapsort(A):

    # construct max heap
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heap_adjust(A, i)
    
    # sort
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_adjust(A, end=i)
    
    return A

# test
if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(heapsort(a))
```

## 参考

[十大经典排序](https://www.cnblogs.com/onepixel/p/7674659.html)

[二叉堆](https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/er-cha-dui-xiang-jie-shi-xian-you-xian-ji-dui-lie)

## 练习

- [ ] 手写快排、归并、堆排序

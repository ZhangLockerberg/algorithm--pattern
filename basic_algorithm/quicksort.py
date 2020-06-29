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
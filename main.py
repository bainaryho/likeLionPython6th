def insertion_sort(arr, start, end):
# insertion 는 arr배열, i, 배열의길이-1또는 2+i의 값중 작은것을 받는다
    for i in range(start + 1, end + 1):
        key_item = arr[i]
        j = i - 1
        while j >= start and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def merge(arr, start, mid, end):
    if arr[mid - 1] < arr[mid]:
        return

    left = arr[start:mid]
    right = arr[mid:end]

    k = start
    i = 0
    j = 0

    while start + 1 < mid and mid + j < end:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if start + i < mid:
        arr[k:end] = left[i:]
    if mid + j < end:
        arr[k:end] = right[j:]


def timsort(arr): #배열을 받아 sort하는 timsort 정렬
    min_run = 2
    n = len(arr) #배열의 길이 n

    for i in range(0, n, min_run): #0부터 배열의 길이까지 2씩 증가
        insertion_sort(arr, i, min((i + min_run), n - 1))
        #insertion 는 arr배열, i, 배열의길이-1또는 2+i의 값중 작은것을 받는다

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, mid, end)
        size *= 2

    return arr


a = ['f', 'g', 'h', 'z', 's', 'b', 'c', 'd']

print(timsort(a))
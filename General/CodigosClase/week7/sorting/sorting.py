# sorting_bench_simple.py
import time, random

# ---------- Sorting algorithms ----------
def bubble_original(a):
    a = a[:]  # copy
    n = len(a)
    for _ in range(n):
        for j in range(n - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def bubble_enhanced(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def selection_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def quicksort(a):
    if len(a) <= 1:
        return a[:]
    pivot = random.choice(a)
    left  = [x for x in a if x < pivot]
    mid   = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def mergesort(a):
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

def heapsort(a):
    a = a[:]
    n = len(a)

    def heapify(i, size):
        while True:
            largest = i
            l = 2*i + 1
            r = 2*i + 2
            if l < size and a[l] > a[largest]:
                largest = l
            if r < size and a[r] > a[largest]:
                largest = r
            if largest == i:
                break
            a[i], a[largest] = a[largest], a[i]
            i = largest

    for i in range(n//2 - 1, -1, -1):
        heapify(i, n)
    for end in range(n-1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(0, end)
    return a

# ---------- Benchmark ----------
if __name__ == "__main__":
    N = 2000
    data = [random.randint(0, 10000) for _ in range(N)]
    sorted_data = sorted(data)

    algs = [
        ("bubble_original", bubble_original),
        ("bubble_enhanced", bubble_enhanced),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
        ("quicksort", quicksort),
        ("mergesort", mergesort),
        ("heapsort", heapsort),
    ]

    for case_name, arr in [("random", data), ("already sorted", sorted_data)]:
        print(f"\nCase: {case_name} (n={len(arr)})")
        for name, fn in algs:
            start = time.time()
            out = fn(arr)
            dt = time.time() - start
            print(f"{name:<15} time={dt:.4f}s  correct={out == sorted(arr)}")

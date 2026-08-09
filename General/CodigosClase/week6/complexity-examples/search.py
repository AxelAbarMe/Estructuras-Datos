import random, bisect, time

# --- 1) Linear scan ---
def linear_search(data, target):
    for x in data:
        if x == target:
            return True
    return False

# --- 2) Binary search (requires sorted data) ---
def binary_search(data, target):
    i = bisect.bisect_left(data, target)
    return i < len(data) and data[i] == target

# --- 3) Set membership ---
def set_search(data_set, target):
    return target in data_set


# --- Demo & timing ---
if __name__ == "__main__":
    n = 1_000_000
    data = list(range(n))          # Sorted list [0, 1, 2, ..., n-1]
    data_set = set(data)           # Build once
    target = n - 1                 # Worst case for linear search

    # Time helpers
    def time_it(fn, *args, repeats=1):
        t0 = time.perf_counter()
        ans = None
        for _ in range(repeats):
            ans = fn(*args)
        t1 = time.perf_counter()
        return ans, (t1 - t0) / repeats

    # Compare methods
    ans1, t1 = time_it(linear_search, data, target)
    ans2, t2 = time_it(binary_search, data, target)
    ans3, t3 = time_it(set_search, data_set, target)

    print(f"Target={target}")
    print(f"Linear search: {t1:.6f} sec")
    print(f"Binary search: {t2:.6f} sec")
    print(f"Set search:    {t3:.6f} sec")

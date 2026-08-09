import time, random

# ---------- Algorithms ----------
def has_duplicates_bruteforce(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def has_duplicates_sort(nums):
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

def has_duplicates_set(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

# ---------- Benchmark helpers ----------
def run_and_time(func, nums):
    start = time.perf_counter()
    result = func(nums)
    return result, time.perf_counter() - start

def pretty(sec):
    if sec < 1e-3: return f"{sec*1e6:.2f} µs"
    if sec < 1: return f"{sec*1e3:.2f} ms"
    return f"{sec:.4f} s"

# ---------- Main ----------
if __name__ == "__main__":
    size = 20_000
    nums = [random.randint(0, 100_000) for _ in range(size)]
    # Force a duplicate
    nums[-1] = nums[0]

    print(f"Benchmark: Duplicates check (n={len(nums)})")

    for func in (has_duplicates_bruteforce, has_duplicates_sort, has_duplicates_set):
        result, dt = run_and_time(func, nums)
        print(f"{func.__name__:<25} result={result} time={pretty(dt)}")

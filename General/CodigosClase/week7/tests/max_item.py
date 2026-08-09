import time, random

# ---------- Algorithms ----------
def max_sort(nums):
    nums = sorted(nums)
    return nums[-1]

def max_linear(nums):
    maximum = nums[0]
    for x in nums:
        if x > maximum:
            maximum = x
    return maximum

def max_builtin(nums):
    return max(nums)

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
    nums = [random.randint(0, 1_000_000) for _ in range(100_000)]
    print(f"Benchmark: Max in list (n={len(nums)})")

    for func in (max_sort, max_linear, max_builtin):
        result, dt = run_and_time(func, nums)
        print(f"{func.__name__:<12} result={result} time={pretty(dt)}")

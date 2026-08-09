import time
import random

def two_sum_bruteforce(nums, T):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == T:
                return True
    return False

def two_sum_twoptr(nums, T):
    nums = sorted(nums)   # copy to avoid modifying original
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == T:
            return True
        if s < T:
            i += 1
        else:
            j -= 1
    return False

def two_sum_hash(nums, T):
    seen = set()
    for x in nums:
        if T - x in seen:
            return True
        seen.add(x)
    return False

# Helper to time functions
def run_and_time(func, nums, T):
    start = time.time()
    result = func(nums, T)
    duration = time.time() - start
    print(f"{func.__name__:<20} Result: {result}, Time: {duration:.6f} seconds")

# Random list generator
def generate_random_list(size, value_range):
    return [random.randint(0, value_range) for _ in range(size)]

# Example usage
if __name__ == "__main__":
    # Small test
    nums = generate_random_list(1000, 10_000)
    T = nums[0] + nums[1]  # guaranteed to exist

    print(f"List size: {len(nums)}, Target: {T}")
    run_and_time(two_sum_bruteforce, nums, T)
    run_and_time(two_sum_twoptr, nums, T)
    run_and_time(two_sum_hash, nums, T)


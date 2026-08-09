from math import isqrt
from time import perf_counter

# 1) O(n)
def is_prime_naive(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

# 2) O(√n)
def is_prime_sqrt(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True

# 3) Sieve
def sieve(max_n):
    primes = [False, False] + [True] * (max_n - 1)
    for p in range(2, isqrt(max_n) + 1):
        if primes[p]:
            for multiple in range(p*p, max_n + 1, p):
                primes[multiple] = False
    return primes

# ---- Demo ----
if __name__ == "__main__":
    test_ns = [10_007, 50_021, 100_003, 200_003, 400_009]

    # Build sieve once
    max_n = max(test_ns)
    t0 = perf_counter()
    sieve_table = sieve(max_n)
    sieve_build = perf_counter() - t0

    for n in test_ns:
        # naive
        t0 = perf_counter(); is_prime_naive(n); naive_t = perf_counter() - t0
        # sqrt
        t0 = perf_counter(); is_prime_sqrt(n); sqrt_t = perf_counter() - t0
        # sieve query
        t0 = perf_counter(); sieve_table[n]; sieve_t = perf_counter() - t0

        print(f"n={n}: naive={naive_t:.4f}s, sqrt={sqrt_t:.4f}s, sieve_build={sieve_build:.4f}s, sieve_query={sieve_t:.6f}s")

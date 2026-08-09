def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)


# Example
print("Sum of 1 to 5:", sum_n(5))   # 15

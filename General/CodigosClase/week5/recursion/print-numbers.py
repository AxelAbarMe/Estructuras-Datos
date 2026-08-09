def print_1_to_n(n):
    if n == 0:   # base case
        return
    print_1_to_n(n - 1)
    print(n)


def print_n_to_1(n):
    if n == 0:   # base case
        return
    print(n)
    print_n_to_1(n - 1)


# Example
print("From 1 to 5:")
print_1_to_n(5)

print("From 5 to 1:")
print_n_to_1(5)


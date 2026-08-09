def count_chars(s):
    if s == "":       # base case: empty string
        return 0
    return 1 + count_chars(s[1:])   # count first char + rest


# Example
print(count_chars("hello"))   # 5
print(count_chars(""))        # 0
print(count_chars("Python"))  # 6

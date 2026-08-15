def reverse_string(s: str) -> str:
    """Return the reversed string using recursion."""
    print(f"reverse_string llamado con: '{s}'")
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome using recursion."""
    print(f"is_palindrome llamado con: '{s}'")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

if __name__ == "__main__":
    print(reverse_string("hello"))      # expected: "olleh"
    print()
    print(is_palindrome("racecar"))     # expected: True
    print()
    print(is_palindrome("python"))      # expected: False
    print()
    print(reverse_string(""))
    print()
    print(is_palindrome(""))
    print()
    print(reverse_string("a"))
    print()
    print(is_palindrome("a"))
    print()
    print(reverse_string("abba"))
    print()
    print(is_palindrome("abba"))
    print()
    print(reverse_string("abc"))
    print()
    print(is_palindrome("abc"))

# Un caso base es la condición que permite a la recursión parar cuando ya cumpla con el objetivo del código
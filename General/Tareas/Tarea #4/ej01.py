import sys

def bin_dec(bin):
    if bin==0:
        return 0
    return (bin%10) + 2 * bin_dec(bin//10)

def main():
    if len(sys.argv) > 1:
        bin = int(sys.argv[1])
        print(bin_dec(bin))
    else:
        print("Error. Requiere Argumento")

if __name__ == "__main__":
    main()

# 1111 / 10 = 111.1 = 111
# 111 / 10 = 11.1 = 11
# 11 / 10 = 1.1 = 1
# 1 / 10 = 0.1 = 0
# 0 END

# 1111
# bin_dec(1111) = 1111 % 10 = 1 + 2(bin_dec(111)) = 1 + 2(7) = 15  ^
# bin_dec(111)  = 111 % 10  = 1 + 2(bin_dec(11))  = 1 + 2(3) = 7   |
# bin_dec(11)   = 11 % 10   = 1 + 2(bin_dec(1))   = 1 + 2(1) = 3   |
# bin_dec(1)    = 1 % 10    = 1 + 2(bin_dec(0))   = 1 + 2(0) = 1   |

# 1010
# bin_dec(1010) = 1010 % 10 = 0 + 2(bin_dec(101)) = 0 + 2(5) = 10  ^
# bin_dec(101)  = 101 % 10  = 1 + 2(bin_dec(10))  = 1 + 2(2) = 5   |
# bin_dec(10)   = 10 % 10   = 0 + 2(bin_dec(1))   = 0 + 2(1) = 2   |
# bin_dec(1)    = 1 % 10    = 1 + 2(bin_dec(0))   = 1 + 2(0) = 1   |
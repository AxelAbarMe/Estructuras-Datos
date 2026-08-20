import sys

def dec_bin(dec):
    if dec==0:
        return 0
    return (dec % 2) + 10 * dec_bin(dec//2)


def main():
    if len(sys.argv) > 1:
        dec = int(sys.argv[1])
        print(dec_bin(dec))
    else:
        print("Error. Requiere Argumento")


if __name__ == "__main__":
    main()


# 15
# dec_bin(15) = 15 % 2 = 1 + 10(dec_bin(7)) = 1 + 10(111) = 1111  ^
# dec_bin(7)  = 7  % 2 = 1 + 10(dec_bin(3)) = 1 + 10(11)  = 111   |
# dec_bin(3)  = 3  % 2 = 1 + 10(dec_bin(1)) = 1 + 10(1)   = 11    |
# dec_bin(1)  = 1  % 2 = 1 + 10(dec_bin(0)) = 1 + 10(0)   = 1     | 
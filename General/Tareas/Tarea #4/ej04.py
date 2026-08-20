import sys

def inversor(num, inv=0):
    if num==0:
        return inv
    return inversor(num//10, inv*10 + num%10)


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        print(inversor(num))
    else:
        print("Error. Requiere Argumento")


if __name__ == "__main__":
    main()


# 1234
# num%10 = 4, inv(123) = 0*10 + 4 = 4
# num%10 = 3, inv(12) = 4*10 + 3 = 43
# num%10 = 2, inv(1) = 43*10 + 2 = 432
# num%10 = 1, inv(0) = 432*10 + 1 = 4321
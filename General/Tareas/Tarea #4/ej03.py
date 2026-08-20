import sys

def div(dividendo, divisor):
    if dividendo < divisor:
        return 0
    return 1 + div(dividendo-divisor,divisor)

def main():
    if len(sys.argv) > 2:
        div1,div2 = int(sys.argv[1]), int(sys.argv[2]) 
        print(div(div1,div2))
    else:
        print("Error. Requiere Argumento")


if __name__ == "__main__":
    main()

# 10, 2
# div(10,2) -> 10<2 false, 1 + div(8,2) -> 1 + 1 + div(6,2) -> 1+1+1+div(4,2) ->...->1+1+1+1+1 = 5
# Contador de cuantas veces cabe

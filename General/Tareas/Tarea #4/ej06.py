import sys

def permutaciones(caracteres):
    if len(caracteres) <= 1:
        return [caracteres]

    result = []

    for i in range(len(caracteres)):
        caracter = caracteres[i]
        sobrante = caracteres[:i] + caracteres[i+1:]
        for permu in permutaciones(sobrante):
            result.append(caracter + permu)

    return result

def main():
    if len(sys.argv) > 1:
        caracteres = sys.argv[1]
        print(permutaciones(caracteres))
    else:
        print("Error. Requiere Argumento")


if __name__ == "__main__":
    main()


# abc
# [a]bc
# [a]cb  2
# [b]ac
# [b]ca  4
# [c]ab
# [c]ba  6
# END

# sobrante = i=0 [:0] = ""
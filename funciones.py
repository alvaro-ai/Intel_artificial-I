import math
def print_mundo(mundo):
    lenx = mundo.totalX
    leny = mundo.totalY
    fin = ""
    valor = ""
    for i in range(0, lenx):
        print("[", end="")
        for j in range(0, leny):
            if j != leny - 1:
                fin = ","
            else:
                fin = "]"
            if mundo.world[i][j] == 1:
                    valor = "░"
            if mundo.world[i][j] == 0:
                    valor = " "
            if i == mundo.peterX and j == mundo.peterY:
                valor = "P"
            print(valor, end=fin)
        print("")
    print("-----------------------------")

def redondeo(x):
    if (math.floor(x) + 0.5) < x:
        return math.ceil(x)
    return math.floor(x)

#!/usr/bin/env python3

#Para repetir 100 veces y sacar el promedio de extracciones de naipes:
#
#    for a in `seq 100`; do ./naipesRepetidos.py -n 100; done | awk '{ s += $0 } END { print s / NR }'
#

import random
import sys

def main():
    args = sys.argv[1:]

    SHOW_ONLY_ITERATIONS = False
    FIND_N_DUPS = 1
    MAX = 5
    for arg in args:
        if arg == "-h" or arg == "--help":
            print("Cantidad de extracciones de naipes hasta coincidir. Pasar cantidad de naipes.")
            print("Ejemplo:  " + sys.argv[0] + " 5")
            print("Pasar -n para tener solo las iteraciones:  " + sys.argv[0] + " -n 100")
            print("Pasar --findn=3 para hallar mas naipes en el mismo experimento.")
            exit()
        if arg == "-n":
            SHOW_ONLY_ITERATIONS = True
            continue
        try:
            if str(int(arg)) == arg:
                MAX = int(arg)
        except ValueError:
            pass
        if arg.startswith("--findn="):
            SHOW_ONLY_ITERATIONS = True
            FIND_N_DUPS = int(arg[len("--findn="):])


    repetidos = set()
    i = 0
    foundN = 0
    while True:
        i += 1
        if not SHOW_ONLY_ITERATIONS and (i % 10000) == 0:
            print(".", end='')
        n = int(random.uniform(1, MAX))
        if n in repetidos:
            foundN += 1
            if SHOW_ONLY_ITERATIONS:
                print(str(i) + " ", end="")
                if FIND_N_DUPS == foundN:
                    print("")
                    break
            else:
                print("Encontrado naipe repetido en solo "
                      + str(i) + " iteraciones. Fue el " + str(n))
                break
        if not SHOW_ONLY_ITERATIONS and i < 10:
            print(n)
        repetidos.add(n)


main()



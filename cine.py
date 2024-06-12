import os


def limpiar_pantalla():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def mostrar_sillas(matriz):
    limpiar_pantalla()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()


def iniciar_sala():
    sillas = []
    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for i in range(len(filas)):
        fila = []
        for j in range(10):
            fila.append(filas[i] + str(j + 1))
        sillas.append(fila)
    return sillas

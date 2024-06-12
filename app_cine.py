import cine
import time

opcion = ''
sillas = cine.iniciar_sala()
cine.limpiar_pantalla()
while opcion != 'N':
    opcion = input("Desea reservar (s/n) ").upper()
    if opcion == 'S':
        cine.mostrar_sillas(sillas)
        silla_deseada = input('Ingrese la silla que desea reservar: ').upper()
        existe = False
        for i in range(len(sillas)):
            for j in range(len(sillas[i])):
                if (sillas[i][j])[:-1] == silla_deseada and (sillas[i][j])[-1] == '*':
                    print("La silla está ocupada")
                    time.sleep(2)
                    existe = True
                    break
                elif sillas[i][j] == silla_deseada:
                    sillas[i][j] += '*'
                    existe = True
                    break
            if existe:
                break
        if not existe:
            print('La silla no existe')
            time.sleep(2)
        cine.mostrar_sillas(sillas)
    elif opcion == 'N':
        print('GRACIAS')
    else:
        print('Opción no encontrada')

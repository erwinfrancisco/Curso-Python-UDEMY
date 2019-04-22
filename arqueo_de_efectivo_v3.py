import time
print('''
******************************************************************************

                    A R Q U E O    D E    E F E C T I V O

******************************************************************************
''')

localtime = time.asctime(time.localtime(time.time()))

print("Fecha :", localtime)
print('\n')

while True:
    print('Selecciona una opcion del siguiente indice ')
    print('''\n
    1) Arqueo de efectivo
    2) Registro de ingresos
    3) Salir del programa''')
    opcion=input()
    if opcion == '1':
        print('\n')
        print('BIENVENIDO AL ARQUEO DE EFECTIVO')
        print('\n')
        def arqueo_de_efectivo(x):
            while True:
                try:
                    i = float(input(x))
                    return i
                    break
                except ValueError:
                    print('Ingresa solo números por favor!')

        aux1 = float(arqueo_de_efectivo( 'Cantidad de monedas: '))
        aux2 = float(arqueo_de_efectivo('Cantidad de billetes de $20: ')*20)
        aux3 = float(arqueo_de_efectivo('Cantidad de billetes de $50: ')*50)
        aux4 = float(arqueo_de_efectivo('Cantidad de billetes de $100: ')*100)
        aux5 = float(arqueo_de_efectivo('Cantidad de billetes de $200: ')*200)
        aux6 = float(arqueo_de_efectivo('Cantidad de billetes de $500: ')*500)
        aux7 = float(arqueo_de_efectivo('Cantidad de billetes de $1000: ')*1000)

        total = (aux1+aux2+aux3+aux4+aux5+aux6+aux7)

        print('\nEl total del arqueo de efectivo es: ', total)

        tlibros = float(input('Ingresa el monto del Registro Contable del celular: '))
        diferencia = (total-tlibros)

        if diferencia > 0:
            print('\nCantidad Sobrante: ', diferencia)
        elif diferencia < 0:
            print('\nCantidad faltante: ', diferencia)
        else:
            print('\nNo existe diferencia: ', diferencia)
        print('\n')
        print('*** Ha finalizado el programa de arqueo de efectivo ***')
        print('\n')
        export = (localtime, float(total), float(diferencia))
        f = open('arqueo_de_efectivo.txt', 'a')
        f.write(str(export)+'\n')
        f.close()

    elif opcion == '2':
        print('En construccion')

    elif opcion == '3':
        print('Fin del programa')
        break
    else:
        print('Has seleccionado una opcion no valida')

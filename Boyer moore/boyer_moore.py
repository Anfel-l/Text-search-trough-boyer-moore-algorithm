
from filemanipulation import file_read



CHAR_NUMBER = 256

def prefijo_malo(cadena, tamaño):

    '''
    Esta función permite calcular las posiciones de los prefijos malos
    o tabla 'd1' a través del patrón y de su tamaño
    
    
    '''

    bad_prefix  =[-1]*CHAR_NUMBER

    for i in range(tamaño):
        bad_prefix[ord(cadena[i])]=i;
    
    return bad_prefix


def boyer_moore(cadena, patron):

    '''
    
    Implementación de código para el algoritmo boyer moore
    código implementado desde: www.facebook.com/atul.kr.007
    autor: Atul Kamar


    En esta clase, se implementa el algoritmo de boyer moore en python
    tomando como puntos claves la longitud de ambas cadenas (patrón, cadena),
    la tabla de prefijos malos implementada de la función anterior y un indice que
    representa el caracter del patrón a encontrar, esto con el fin de compararlo con
    la cadena y encontrar la coincidencia

    '''
    
    coincidencias = []
    
    
    
    x=len(patron)
    y=len(cadena)

    bad_prefix = prefijo_malo(patron, x)
    aux_indexP = 0

    while ( aux_indexP <= y-x):
        aux_index = x-1

        while aux_index >= 0 and patron[aux_index] == cadena[aux_indexP+aux_index]:
            aux_index -= 1

        if aux_index < 0:
            print("El patrón ha sido encontrado en el índice = {}".format(aux_indexP)) 
            coincidencias.append(aux_indexP)
            
            aux_indexP += (x-bad_prefix[ord(cadena[aux_index+aux_indexP])] if aux_index+x<y else 1)
        
        else:
            aux_indexP += max(1, aux_index-bad_prefix[ord(cadena[aux_indexP+aux_index])])
        
    return coincidencias

def select(cadena, patron, coincidencias=[]):

    nueva_cadena=[]
    
    aux_cadena=[]


    aux_list=[]

    aux_list.append(coincidencias)
    aux_char=len(patron)
    aux_cadena.append(cadena)
    cadeana_copy=aux_cadena[:]
    

    
    
    aux_index2=0
    for itm in aux_list:
        for itm2 in itm:
            if itm.index(itm2) != 0:

                itm2 += len(aux_cadena[aux_index2]) - len(cadeana_copy[aux_index2])
            
            aux_cadena[aux_index2] = aux_cadena[aux_index2][0:itm2] + "[" + aux_cadena[aux_index2][itm2:(itm2 + aux_char)] + "]" + aux_cadena[aux_index2][(itm2 + aux_char):]
        nueva_cadena.append(aux_cadena[aux_index2])
        aux_index2 += 1

    return nueva_cadena




def switch():
    '''
    Esta función permite elegir el método de entrada
    a través de una serie sencilla de condicionales

    1. La opción número 1 le permite al usuario introducir la cadena por consola
    2. La opción número 2 le permite al usuario introducir la cadena a través de un
       archivo de texto importado desde una ruta
    
    en ambas situaciones se muestran los indicies en los cuales fue encontrado el
    patrón

    '''

    print("Elige una opción para la búsqueda: " )
    print("1. Introducir cadena y patrón")
    print("2. Importar cadena desde archivo de texto")
    
    op = int(input("===> Introduce opción: "))

    if op == 1:
        aux1 = input(str("Introduce cadena madre: "))
        aux2 = input(str("Introduce el patrón: "))

        print(select(aux1, aux2, boyer_moore(aux1, aux2)))
    elif op == 2:
        aux1 = input(str("Introduce fichero: "))
        aux2 = input(str("Introduce patron: "))
        
        cadena = str(file_read(aux1))

        print(select(cadena, aux2, boyer_moore(cadena, aux2)))

    


def main():
    switch()

if __name__ == '__main__':
    main()




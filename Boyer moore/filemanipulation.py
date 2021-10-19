def file_read(archivo, modo):
    '''
    Esta función permite leer un archivo desde el ordenador
    y obtiene su contenido en forma de string.

    '''
    aux1=str(archivo)
    aux2=str(modo)

    f = open(archivo, modo)
    lines  = f.readlines()
    print(lines)
    return lines

    

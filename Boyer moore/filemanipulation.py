def file_read(archivo):
    '''
    Esta función permite leer un archivo desde el ordenador
    y obtiene su contenido en forma de string.

    '''
    
    with open(archivo) as file_object:
        contents = file_object.read()
    

    
    return contents

    

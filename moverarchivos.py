import os
import shutil

dedonde = "C:/Users/diana/prueba"
adonde = "C:/Users/diana/Documents/Python/c102"

listadearchivos = os.listdir(dedonde)
print(listadearchivos)

for nombre in listadearchivos: 
    name,extension = os.path.splitext(nombre)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.doc', '.docx']:
        #Ubicacion del archivo que voy a mover
        path1 = dedonde + '/' + nombre
        #Creo la carpeta a donde lo voy a mover
        path2 = adonde + '/' + "ArchivosMovidos"
        #Ruta del archivo dentro de la carpeta nueva
        path3 = adonde + '/' + "ArchivosMovidos" +'/' + nombre

        print ("path1", path1)
        print ("path3", path3)

        #checa si las rutas existen en el equipo. si no, crea una carpta nueva y muevelo
        if os.path.exists(path2):
            print("Moviendo Archivo")
            #mueve el archivo
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moviendo " + nombre + ".....")
            shutil.move(path1, path3)
        
        
        
    

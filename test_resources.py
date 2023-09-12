import os

if not os.path.exists('resources'):
    raise Exception('La carpeta resources no se ha descargado correctamente')

import os
import subprocess
import sys

# DESCARGADOR DE PLAYLISTS DE SPOTIFY por saultj
# Instrucciones:
# - Tener instalado la librería spotdl (pip3 install spotdl) (quizás al ejecutarlo te pide otros requisitos)
# - Especificas la url (Asegurate que es visible y no es privada, sino no se podrá localizar)
# - Especificas la ruta donde quieres realizar la descarga (ruta absoluta, cuidado con la codificación con \ )
# Tarda un ratillo pero se bajan en calidad bastante solida
# Si eres un prisas puedes configurar tu acceso a la api con una app de spotify devs (buena suerte)

def main():
    # Comprueba si tienes spotdl
    print("Comprobando si tienes spotdl y sus dependencias...")
    try:
        resultado = subprocess.run(["spotdl", "--version"], check=True, capture_output=True, text=True)
        print(f"Bien bro lo tienes, versión: {resultado.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        instalar= input("No lo tienes instalado jefe, quieres? (s/n)\n-> ")
        if instalar == 's':
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "spotdl"], check=True)
                print("Instalado correctamente socio, ya puedes seguir")
            except subprocess.CalledProcessError:
                print("Error al instalar.")
                sys.exit(1)
        else:
            print("Pues nada tu no lo instales")
            sys.extit(1)
                        

    playlist_url = input("URL de tu playlist (que sea publica por favor):\n-> ").strip()
    download_path = input("Ruta para descargar (ruta ABSOLUTA):\n-> ").strip()

    # Chekea la ruta
    if not os.path.exists(download_path):
        crear = input(f"Tu ruta '{download_path}' no existe. ¿Quieres crearla? (s/n):\n->  ").strip().lower()
        if crear == 's':
            os.makedirs(download_path)
            print(f"Ruta '{download_path}' creada con éxito.")
        else:
            print("Sin ruta válida no se puede, espabila chaval.")
            return

    # Ejecutamos spotdl para proceder con la descarga
    try:
        print("Descargando tus canciones...")
        # Aquí configuramos una calidad premium y la ruta de descarga
        subprocess.run(["spotdl", "--bitrate", "320K", "--output", download_path, playlist_url], check=True)
        print("Disfruta tus temas rey")
    except subprocess.CalledProcessError:
        print("Error al descargar (Has instalado spotdl?) (La playlist es publica?)")

if __name__ == "__main__":
    main()
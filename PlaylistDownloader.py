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
        instalar = input("No lo tienes instalado jefe, quieres? (s/n)\n-> ")
        if instalar == 's':
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "spotdl"], check=True)
                print("Instalado correctamente socio, ya puedes seguir")
            except subprocess.CalledProcessError:
                print("Error al instalar. Revisa tu entorno python chaval.")
                sys.exit(1)
        else:
            print("Pues nada tu no lo instales")
            sys.exit(1)

    # Recoge las playlists
    playlist_urls = []
    while True:
        playlist_url = input("URL de tu album o playlist (que sea publica por favor):\n-> ").strip()
        playlist_urls.append(playlist_url)
        
        otra = input("¿Quieres añadir más? (s/n):\n-> ").strip().lower()
        if otra != 's':
            break
    
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

    # Descargamos cada playlist
    for i, playlist_url in enumerate(playlist_urls, 1):
        try:
            print(f"\nDescargando lista {i} de {len(playlist_urls)}...")
            # Aquí configuramos una calidad premium y la ruta de descarga
            subprocess.run(["spotdl", "--bitrate", "320K", "--output", download_path, playlist_url], check=True)
            print(f"Playlist {i} descargada con éxito")
        except subprocess.CalledProcessError:
            print(f"Error al descargar la playlist {i} (¿La playlist es publica? ¿Has puesto bien el link?)")
            continue
    
    print("\n¡Proceso completo! Disfruta tu music rey")

if __name__ == "__main__":
    main()
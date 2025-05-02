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
    # Print Banner
    print(r'''
   _____             _           _          __  __ _____ ____  
  / ____|           | |         | |        |  \/  |  __ \___ \ 
 | (___  _ __   ___ | |_ _   _  | |_ ___   | \  / | |__) |__) |
  \___ \| '_ \ / _ \| __| | | | | __/ _ \  | |\/| |  ___/|__ < 
  ____) | |_) | (_) | |_| |_| | | || (_) | | |  | | |    ___) |
 |_____/| .__/ \___/ \__|\__, |  \__\___/  |_|  |_|_|   |____/ 
        | |               __/ |                                
        |_|              |___/                                 
''')

    # Comprueba si tienes spotdl
    awn = input("[x] Tienes inatado spotdl? (s/n) Si no te lo instalo rapidito socio\n-> ")
    if(awn == 'n'):
        try:
            resultado = subprocess.run(["spotdl", "--version"], check=True, capture_output=True, text=True)
            print(f"[x] Bro ya lo tenías, versión: {resultado.stdout.strip()}")
        except (subprocess.CalledProcessError, FileNotFoundError):
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", "spotdl"], check=True)
                    print("Instalado correctamente socio, ya puedes seguir")
                except subprocess.CalledProcessError:
                    print("Error al instalar. Revisa tu entorno python chaval.")
                    sys.exit(1)
    else:
        print("[x] Omitiendo instalación...")


    # Recoge las playlists
    playlist_urls = []
    print("[x] Puedes poner enlaces a listas o albumes, o introducir el titulo + artista de un tema y quizás funcione")
    while True:
        playlist_url = input("[x] URL de tu album o playlist (que sea publica por favor):\n-> ").strip()
        playlist_urls.append(playlist_url)
        
        otra = input("[x] ¿Quieres añadir más? (s/n):\n-> ").strip().lower()
        if otra != 's':
            break
    
    download_path = input("[x] Ruta para descargar (ruta ABSOLUTA):\n-> ").strip()

    # Chekea la ruta
    if not os.path.exists(download_path):
        crear = input(f"[x] Tu ruta '{download_path}' no existe. ¿Quieres crearla? (s/n):\n->  ").strip().lower()
        if crear == 's':
            os.makedirs(download_path)
            print(f"[x] Ruta '{download_path}' creada con éxito.")
        else:
            print("[x] Sin ruta válida no se puede, espabila chaval.")
            return

    # Descargamos cada playlist
    for i, playlist_url in enumerate(playlist_urls, 1):
        try:
            print(f"\n[x] Descargando lista {i} de {len(playlist_urls)}...")
            # Aquí configuramos una calidad premium y la ruta de descarga
            subprocess.run(["spotdl", "--bitrate", "320K", "--output", download_path, playlist_url], check=True)
            print(f"[x] Playlist {i} descargada con éxito")
        except subprocess.CalledProcessError:
            print(f"[x] Error al descargar la playlist {i} (¿La playlist es publica? ¿Has puesto bien el link?)")
            continue
    
    print("\n[x] ¡Proceso completo! Disfruta tu music rey")

if __name__ == "__main__":
    main()
# Spotify Playlist Downloader 🎵

A simple, fun, and straightforward Python script to download Spotify playlists in high quality (320kbps MP3).  
Built for those who want an easy, no-nonsense solution.

## Features 🚀
- Checks if `spotdl` is installed and offers to install it automatically.
- Downloads public Spotify playlists to a chosen folder.
- Ensures playlist quality at 320kbps.
- Friendly and clear console messages — no weird jargon.

## Requirements 📦
- Python 3.x installed
- Internet connection
- `spotdl` library (installed automatically if missing)

## Installation ⚙️
Clone this repository:
```bash
git clone https://github.com/yourusername/spotify-playlist-downloader.git
cd spotify-playlist-downloader
```

(Optional) Install manually:
```bash
pip install spotdl
```
Or just run the script and it will guide you.

## Usage 🎧
1. Open your terminal.
2. Execute the script:
   ```bash
   python downloader.py
   ```
3. Follow the prompts:
   - Paste your **public** Spotify playlist URL.
   - Choose your absolute download path.
4. Done! Songs will be downloaded at premium quality.

⚡ **Notes**:
- Private playlists are not supported unless you configure Spotify API credentials.
- Internet connection required.

## Troubleshooting 🛠
- Ensure your playlist is public and the link is valid.
- Allow the script to create a new download directory if needed.
- If problems persist, reinstall `spotdl` or check your Python environment.

## License 📜
This project is licensed under the **Apache License 2.0** — see the [LICENSE](./LICENSE) file for details.  
All respect to the [spotDL](https://github.com/spotDL/spotify-downloader) team for the heavy lifting.

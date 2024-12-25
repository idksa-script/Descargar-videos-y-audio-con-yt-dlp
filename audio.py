import yt_dlp

def audio(link):
    formato = {
        "outtmpl": "%(title)s.%(ext)s",  # Correcto
        "format": "bestaudio/best",           # Correcto
        "postprocessors": [{
            "key": "FFmpegExtractAudio",  # Correcto
            "preferredcodec": "mp3",        # Corregido: "preferrecodec" -> "preferredcodec"
            "preferredquality": "192",       # Corregido: "preferrequality" -> "preferredquality"
        }],
    }

    with yt_dlp.YoutubeDL(formato) as yt:
        yt.download([link])

    print("Proceso terminado")



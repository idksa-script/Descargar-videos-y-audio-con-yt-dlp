import yt_dlp
def video(link):
    formato = {
            "outtmpl": "%(title)s.%(ext)s",
            "format": "best"
            }
    with yt_dlp.YoutubeDL(formato) as yt:
        yt.download([link])

    print("Proceso terminado")


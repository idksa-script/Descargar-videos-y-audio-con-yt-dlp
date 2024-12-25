import yt_dlp
from video import video
from audio import audio

link = input("Ingresa el link de lo que quieres descargar: ")

print("Elige una de las opciones}\n\tDescargar video\n\tDescargar solo audio(mp3)")

eleccion = int(input("Ingresa una de las opciones: "))

if eleccion == 1:
    video(link)
elif eleccion == 2:
    audio(link)
else:
    print("Ingresa solo una de las opciones dadas")

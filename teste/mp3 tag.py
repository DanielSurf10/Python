import eyed3
from os import listdir

a = listdir("/home/daniel/OutrasCoisas/músicas/Instrumental/deemix Music/Aagitada/")

for i in a:
    audiofile = eyed3.load(f"/home/daniel/OutrasCoisas/músicas/Instrumental/deemix Music/Aagitada/{i}")
    audiofile.tag.artist = "Agitada"
    print(audiofile.tag.artist)

    audiofile.tag.save()


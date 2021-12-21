from os import chdir, getcwd, listdir, system

cam = input('Digite o caminho: ')

chdir(cam)
print(getcwd())

for c in listdir():
    system(f"lpr -P HP_Deskjet_4640_series_69E76D '{c}'")


# c.replace(" ", "\\ ")

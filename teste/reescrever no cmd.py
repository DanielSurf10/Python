from time import sleep
import sys

def Print(texto = ''):
    sys.stdout.write("\r" + texto)
    sys.stdout.flush()

sys.stdout.write("oi")
sleep(1)
Print()
sys.stdout.write("io")

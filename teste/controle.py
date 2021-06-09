import pyvjoy
import serial

# Coisas
vjoy  = 1
porta = "COM9"
contador = 0
deslocador = 1

# Tamanho = 48

controle = pyvjoy.VJoyDevice(vjoy)
arduino = serial.Serial(porta)

arduino.readline()
arduino.readline()
# print(lido)

while True:
    botao = int(arduino.readline()[:-2])
    analogico = int(arduino.readline()[:-2])

    # Botão
    # for i in range(17):
    #     if (botao & deslocador) > 0:
    #         print(1, end=' ')
    #     else:
    #         print(0, end=' ')
    #     deslocador = deslocador << 1

    # Analógico
    print(analogico & 255)
    # analogico = analogico >> 16


    deslocador = 1

# while True:
#     botao = int(arduino.readline()[:-2])
#     analogico = int(arduino.readline()[:-2])

#     print(botao, analogico)

# for i in range(48):
#     lido = int(arduino.readline()[:-2])
#     print(lido & (1 << 48 - i), end=' ')


# controle.set_button(2, 1)

# while True:
#     lido = int(arduino.readline()[:-2])
    
#     controle.set_button(1, lido & 1)

arduino.close()

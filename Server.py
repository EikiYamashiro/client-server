#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação Server
####################################################

from enlace import *
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    try:
        com2 = enlace('COM2') #Arduino 2
        com2.enable() 

        #Recebe o tamanho da imagem
        print("Recebendo o tamanho da imagem...")
        
        image_size_bytes, nRx = com2.getData(4)
        
        print("Tamanho em bytes: ",image_size_bytes)
        
        image_size_int = int.from_bytes(image_size_bytes, byteorder='big')
        
        print("Tamanho em inteiros: ",image_size_int)

        print("-------------------------------------")
        print("Recebendo a imagem...")
        rxBufferServer, nRxServer = com2.getData(image_size_int)
        sizeServer = nRxServer
        sizeServerBytes = nRxServer.to_bytes(4, byteorder='big')
        com2.sendData(sizeServerBytes)
        time.sleep(0.1)
        print("-------------------------------------")
        print("Comunicação encerrada")
        print("-------------------------------------")
        com2.disable()  
    except:
        print("ops! :-\\")
        com2.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()

#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação Client
####################################################

from enlace import *
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    try:
        #Enlace com COM1
        com1 = enlace('COM1') 
        com1.enable()
        #Abre a interface para o usuário selecionar a imagem
        print('Escolha uma imagem:')
        Tk().withdraw()
        image_selected = askopenfilename(filetypes=[("Image files", ".png .jpg .jpeg")])
        print("Imagem selecionada: {}".format(image_selected))
        imageR = image_selected

        #Carrega a imagem para a transmissão
        print("Carregando imagem pra transmissão...")
        print("-----------------------------------")
        txBufferClient = open(imageR, 'rb').read()
        size_real = len(txBufferClient)
        txSizeClient = len(txBufferClient).to_bytes(4, byteorder='big') #esse método é mais rápido do que o getStatus()
        time_start = time.time()

        #Enviando o tamanho da imagem
        com1.sendData(txSizeClient)
        print("Mandando tamanho da imagem para o Server...")
        time.sleep(0.1)
        print("-----------------------------------")
        com1.sendData(txBufferClient)
        print("Mandando imagem para o Server...")
        time.sleep(0.1)
        print("-----------------------------------")
        rxBufferClient, nRxClient = com1.getData(4)
        size_server = int.from_bytes(rxBufferClient, byteorder='big')
        print("Tamanho da imagem: {}".format(size_server))
        
        if size_server == size_real:
            time_end = time.time()
            print("Transferência de dados feita com sucesso!")
            time_total = time_end - time_start
            taxa_transmissão = size_real/time_total
            print("-----------------------------------")
            print("Tempo gasto: {} segundos".format(time_total))
            print("Taxa de Transmissão: {} [bytes/s]".format(taxa_transmissão))
        
        else:
            print("Ocorreu um erro na transferência de dados")
    
        # Encerra comunicação
        com1.disable()
        print("-----------------------------------")
        print("Comunicação encerrada!")
        print("-----------------------------------")
    except:
        print("ops! :-\\")
        com1.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()

import cv2
import numpy as np
import os
import Funcoes



camera = cv2.VideoCapture('http://100.105.82.168:3128/video')    #Chama a camera ZERO indica a camera principal
#camera = cv2.VideoCapture(0)    #Chama a camera ZERO indica a camera principal

Casc_olho = cv2.CascadeClassifier('haarcascade_eye.xml')                    #XML indentificador de olhos
Casc_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    #XML indentificador de face

Nome =  input("Digite seu nome")
ID = Funcoes.AddNome(Nome)


#os.mkdir('Faces/' + Nome, 0o755)        #Cria pasta com o nome
Contador = 1

while(Contador < 50):
    ret, frame = camera.read()   #Pega os frame

    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       #Converte os frame em preto e branco
                                                                                        ## Parametros
    faces = Casc_face.detectMultiScale(frame_cinza, scaleFactor=1.25, minNeighbors=5) ## frame, redução da imagem 1.5 = 50%,


    if np.average(frame_cinza) > 110:  ## minimo de janelas para considerar a ser uma face
        for (x, y, w, h) in (faces):
            print(x, y, w, h)
            cv2.rectangle(frame, (x ,y), ((x+w), (y+h)), (255, 0, 0), 3)     #Cria pinta um retangulo no rosto

            ###Olhos
            Rosto = frame[y:y+h, x:x+w]                                     #Corta Rosto no frame
            Rosto_cinza = cv2.cvtColor(Rosto, cv2.COLOR_BGR2GRAY)           #Rosto em cinza
            Olhos = Casc_olho.detectMultiScale(Rosto_cinza)                 #detecta Olhos

            for(ox, oy, ow, oh) in Olhos:
                cv2.rectangle(Rosto, (ox, oy), ((ox+ow), (oy+oh)), (255, 0, 0), 2) ##Melhor deixar comentado rsrsrs

                #if(cv2.waitKey(1) &0xFF == ord('f')):
                Frame_corte = cv2.resize(frame_cinza[y:y + h, x:x + w], (220, 220))  # Corta Frame(apenas rosto)

                Imagem_cortada = (Nome + "."+ str(ID) +"." + str(Contador) + '.png')            #Nomeia nome da Image cortada

                            #Diretorio       / Nome da imagem  || imagem
                cv2.imwrite('Faces/'+ Nome + '/' + Imagem_cortada, Frame_corte)    #Salva Imagem Cortada
                cv2.waitKey(300)    #Delay para dar tempo de posicionar o rosto para proxima foto
                cv2.imshow("Foto tirada", Frame_corte)      #Foto tira/cortada
                print("Foto Tirada")
                Contador += 1


    cv2.imshow("Reconhecimento facial", frame)          ##Abre os frame na camera

    #cv2.resizeWindow("Reconhecimento facial", 500, 500)
    #if(Contador >= 10):   #Fecha a janela ao pressionar a tecla e
        #break

camera.release()
cv2.destroyAllWindows()

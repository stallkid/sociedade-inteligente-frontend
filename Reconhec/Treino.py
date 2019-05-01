import cv2
import os
import numpy as np

Eigenface = cv2.face.EigenFaceRecognizer_create()
Fisherface =cv2.face.FisherFaceRecognizer_create()
LBPH = cv2.face.LBPHFaceRecognizer_create()

Pasta = 'Faces'
def ImagemID():
    Rostos = []  ##Array para guardar a foto
    IDs = []  ##Array para guardar o id

    for DirPrin, SubDir, NomeFoto in os.walk(Pasta): #Passa pelo diretorio principal, pelo subdiretorios e pelos arquivo(foto)
        for SubPasta in SubDir:             #Pega nomes das sub-pasta da pasta principal
            #print(SubPasta)                                        #Printa os subdiretorio da pasta principal
            EnderecoPasta = os.path.join(DirPrin, SubPasta)         #Forma o endereço das sub-pasta "Face/face1", "Face,face2"
            #print(EnderecoPasta)                                    #printa endereco das pasta


            for Nome_foto in os.listdir(EnderecoPasta):  #Percorre as sub-pasta e pega os nome da foto
                Endereco_foto = EnderecoPasta + "/" + Nome_foto     #Forma endereço das foto  "Face/face1/pessoa1.png", "Face,face2/pessoa2.png"
                #print(Endereco_foto)

                Rosto_img = cv2.cvtColor( cv2.imread(Endereco_foto), cv2.COLOR_BGR2GRAY)        #Pega a Imagem e converte para PRETO e BRANCO
                #Rosto_img = Rosto_img.resize((110, 110))

                ID = int(os.path.split(Endereco_foto)[-1].split('.')[1])                #Fatia a String pegando o ID
                #print(ID)                                       #Print ID das imagens
                IDs.append(ID)              #Adicona ID no array
                Rostos.append(Rosto_img)    #Adicona a foto no array

                #Rosto_img = cv2.imread(Endereco_foto)           #Le as imagem
                #cv2.imshow("la", Rosto_img)                     #pos ler, exibir na tela
                #cv2.waitKey(10)
    return np.array(IDs), Rostos            #Faz array relacionando os rostos com seus ID respéctivos


IDs, Rostos = ImagemID()
#print(IDs)

Eigenface.train(Rostos, IDs)                    #Passa os rostos e IDs para o algoritmo Eigenface treinar
Eigenface.write('classifiacadoreign.xml')       #Pós treino Eigenface salva o aprendizado no arquivo YML
print("fim")

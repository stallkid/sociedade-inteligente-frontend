import cv2
import Funcoes

Casc_olho = cv2.CascadeClassifier('haarcascade_eye.xml')                    #XML indentificador de olhos
Casc_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    #XML indentificador de face

Reconhecedor = cv2.face.EigenFaceRecognizer_create()
Reconhecedor.read("classifiacadoreign.yml")

font = cv2.FONT_HERSHEY_COMPLEX_SMALL

camera = cv2.VideoCapture('http://192.168.43.186:8080/video')    #Chama a camera ZERO indica a camera principal
#camera = cv2.VideoCapture(0)    #Chama a camera ZERO indica a camera principal

while(True):
    ret, frame = camera.read()

    Frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    FacesDetectadas = Casc_face.detectMultiScale(Frame_cinza, 1.25, 5)
    for(x, y, w, h) in FacesDetectadas:
        print(x, y, w, h)
        Face_img = cv2.resize(Frame_cinza[y:y+h, x:x+w], (220, 220))

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        id, confianca = Reconhecedor.predict(Face_img)                  # Reconhece o rosto e joga o id do rosto e o nivel de confiança nas variaveis
        #id = Funcoes.PegaNome(id)
        cv2.putText(frame, str(id), (x, y + (h+30)), font, 2, (255,0 ,0 ))  #Posiciona o ID na imagem da webcam
        cv2.putText(frame, str(confianca), (x, y + (h + 70)), font, 2, (255, 0, 0))  # Posiciona o ID na imagem da webcam

    cv2.imshow("Camera", frame)
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()



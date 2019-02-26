import cv2



cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID') #ou ('X', 'V', 'I', 'D')
out = cv2.VideoWriter('VideoGravado.avi', fourcc, 15.0, (640,480))

while(cap.isOpened()):

    ret, frame = cap.read()   #Frame captura os quadros, ret verifica se é true ou false
    if ret == True:
        frame = cv2.flip(frame, 1)

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.BORDER_TRANSPARENT)  #Cor dos quadro

        cv2.imshow("frame", gray) # Exibe no frame

        if cv2.waitKey(1) & 0xFF == ord('q'): #"espera a tecla "q" para sair"
            break
out.release()
cap.release()
cv2.destroyAllWindows()
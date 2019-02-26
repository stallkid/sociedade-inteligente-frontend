import cv2

img = cv2.imread('ft.jpg', 0)       #carrega Imagem
img1 =cv2.imread("ft1.jpg", -1)

# 1  - cv2.IMREAD_COLOR       #Colorida
# 0  - cv2.IMREAD_GRAYSCALE   #cinza
#-1  - cv2.IMREAD_UNCHANGED    #Origianal


cv2.namedWindow('Imagem', cv2.WINDOW_NORMAL)    #Janela redimensionavel
cv2.imshow('Imagem', img)           #Exibe imagem

cv2.namedWindow("Imagem 1", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Imagem 1", img1)

#k armazena a tecla apertada
k = cv2.waitKey(0)  #Aguarda uma tecla para fechar janelas

if k == 27:             #Compara o ASCII  da tecla se é 27
    print("ESC")
    cont = 0+1
    cv2.imwrite("SALVOU%s.jpg" %(cont), img1)  #Salva imagem no diret/projeto

elif k == ord('s'): #Compara o ASCII da tecla se é o mesmo do S

    cv2.destroyWindow("Imagem")  #fecha janela especifica


    img1 = cv2.imread("ft1.jpg", -1)
    print("S")
    cv2.namedWindow("Imagem 1", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Imagem 1", img1)
    cv2.waitKey(0)


#cv2.destroyAllWindows() #Fecha todas as janelas


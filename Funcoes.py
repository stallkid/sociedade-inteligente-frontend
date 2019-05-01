import os


def AddNome(Nome):

    Nome = Nome
    os.mkdir('Faces/' + Nome, 0o755)
    Texto = open("Nomes.txt", "r+")
    ID = ((sum(1 for line in Texto))+1)
    Texto.write(str(ID) + " " + "," + " " + Nome + "\n")
    print ("Nome salvado com ID " + str(ID))
    Texto.close()

    return ID


def PegaNome(ID):

    with open("Nomes.txt") as TXT:
        for line in TXT:
            test = (line.split(",")[0])
            #print(test)

            if(int(test.strip()) == ID):
                #print(test)
                #ter = (line.split(",")[0])

                Nome = (line.split(",")[1]).strip()
                #print(Nome)

                return Nome

                


#pr = PegaNome(3)

#print(pr)

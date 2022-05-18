filmes = open ("filmes.txt", "r")
filmes_disponiveis = [filmes]
filmes.close ()


def limpar_tela():
    import os
    temp = os.system('cls')



    
def menu ():
    voltar_menu = 's'
    while voltar_menu == 's':
        limpar_tela ()
        opcao = input ('''                                                                                                                                                                  
                                            ~*~*~ BEM VINDO A BLOCKBUSTER ~*~*~ 
                         ~*~*~ ~*~*~ ~*~*~ Você quer alugar ou devolver um filme? ~*~*~ ~*~*~ ~*~*~  
                         
                                ~*~*~ [1] ALUGAR  ~*~*~ ~*~*~ ~*~*~  [2] DEVOLVER  ~*~*~ ~*~*~ ~*~*~ 
                                ~*~*~  ~*~*~ [3] FILMES DISPONIVEIS ~*~*~  ~*~*~ [4] SAIR ~*~*~  ~*~*~
                                                        ~*~*~  ~*~*~ ~*~*~  ~*~*~ 
                                            
                                    ~*~*~ ~*~*~ ~*~*~ ESCOLHA SUA OPÇÃO:    
                        ''')

        if opcao == "1":
            alugar()
        elif opcao == "2":
            devolver()
        elif opcao == "3":
            catalogo()
        elif opcao == "4":
            sair()
        voltar_menu = input("voltar ao menu? S/N ").lower()   

def catalogo ():
    filmes = open ("filmes.txt", "r")
    filmes_disponiveis = []
    for filmes_disponiveis in filmes:
        print (filmes_disponiveis.strip ())

    filmes.close()
        
def alugar():
    filmes = open ("filmes.txt", "r")
    filmes_disponiveis = []
    for filmes_disponiveis in filmes:
        print (filmes_disponiveis.strip ())
    alugar_filme = input ('''                                                                                                                                                                  
                                            ~*~*~ Qual filme você quer alugar ~*~*~ 
                                    ~*~*~ ~*~*~ ~*~*~ ESCOLHA SUA OPÇÃO:    
                        ''')
    
    filmes = open("filmes.txt", "r")
    aux = []
    aux2 = []
    for i in filmes:
        aux.append (i)
    for i in range(0, len (aux)):
        if alugar_filme not in aux [i]:
            aux2.append(aux[i])
            filmes = open ("filmes.txt", "w")
    for i in aux2:
        filmes.write (i)
        print (f'VOCÊ ALUGOU UM FILME!')   

def devolver ():
    devolver_filme = input ("Qual filme deseja devolver? ")
    filmes = open ("filmes.txt", 'r',)
    filmes_disponiveis = [filmes.read ()]
    if devolver_filme not in filmes_disponiveis:
        filmes = open ("filmes.txt", "a")
        filmes.write ("\n{}".format (devolver_filme))
        print ("Você acabou de devolver {}".format(devolver_filme))
    filmes.close () 

def sair ():
    exit()

def locadora ():
    limpar_tela ()
    menu ()
    
if (__name__ == "__main__"):
    locadora ()

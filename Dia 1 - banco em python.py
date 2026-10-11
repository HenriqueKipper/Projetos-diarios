

def depositar(saldo_inicial,valor,extrato):
    if valor > 0:
        saldo_final = saldo_inicial + valor
        
        extrato.append(f'Depositado - R${valor}')

        return saldo_final
    
    else:
        print("Valor incorreto")
        return saldo_inicial

def sacar(saldo_inicial,valor,extrato):

    if saldo_inicial >= valor and valor > 0:
        saldo_final = saldo_inicial - valor
        
        extrato.append(f'Sacado - R${valor}')

        return saldo_final
    
    else:
        print("Valor incorreto")
        return saldo_inicial

def consultar(saldo):
    print(f"Seu saldo é de R${saldo}")

def print_extrato(list):

    print("Extrato:")

    for i in list:
        
        print("\n" + i)
        


def fechar():
    exit()

def limpar_tela():
    for i in range(8):
        print("\n")

def enter_continuar():
    input("\n" + "Precione Enter para continuar")

def main():

    saldo = 1000.00


    extrato = []

    while True:

        print("Bem vindo a o Banco.")
        print("Escolha uma das opções a baixo:")
        print("Digite 1 - Consultar saldo")
        print("Digite 2 - Depositar")
        print("Digite 3 - Sacar")
        print("Digite 4 - Extrato")
        print("Digite 5 - Fechar banco")
        
        
        try: opcao = int(input())
        except ValueError:
            limpar_tela()
            print("Digite um valor valido")
            enter_continuar()
            continue


        if opcao < 1 or opcao > 5:
            
            limpar_tela()

            print("Digite um Numero de 1 a 5")

            enter_continuar()
            
            continue

        if opcao == 1:

            limpar_tela()
            
            consultar(saldo)

            enter_continuar()
        
        elif opcao == 2:

            limpar_tela()
            
            print("Quantidade a depositar: ")

            try: quantidade = float(input())
            except ValueError:
                limpar_tela()
                print("Digite um valor valido")
                enter_continuar()
                continue

            saldo = depositar(saldo,quantidade,extrato)

            

            enter_continuar()
        
        elif opcao == 3:

            limpar_tela()

            print("Quantidade a sacar: ")
            
            try: quantidade = float(input())
            except ValueError:
                limpar_tela()
                print("Digite um valor valido")
                enter_continuar()
                continue
            saldo = sacar(saldo,quantidade,extrato)

           

            enter_continuar()
        
        elif opcao == 4:
            
            limpar_tela()
            
            print_extrato(extrato)

            enter_continuar()
        
        elif opcao == 5:
        
            fechar()
        
        limpar_tela()



if __name__ == "__main__":
    main()
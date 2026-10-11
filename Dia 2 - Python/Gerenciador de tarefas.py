import json

## Gerenciador de tarefas

def escrever_json(arquivo,objeto):

    with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(objeto,arquivo_json)

def ler_json(arquivo):
    
    with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
        return json.load(arquivo_json)

def limpar_tela():
    for i in range(8):
        print("\n")



def main():

    
    while True:

        arquivo_tarefas = "tarefas.json"
        
        try: lista_tarefas = ler_json(arquivo_tarefas)
        
        except FileNotFoundError:
            lista_tarefas = []
        except json.JSONDecodeError:
            print("ARQUIVO TAREFAS CORROMPIDO")
            break
    
        print("===== GERENCIADOR DE TAREFAS =====")
        print("")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        print("")
        print("Escolha uma opção:")

        opcao = input()
        limpar_tela()
        if opcao == "1":

            

            limpar_tela()

            print("Nome da tarefa: ")

            nome = input().strip()
            
            tarefa = {"nome":nome,"concluida":False}

            tarefa_existe = False

            for i in lista_tarefas:
                if i["nome"] == nome:

                    tarefa_existe = True
            
            if tarefa_existe:
                print("Não é permitido criar mais de uma tarefa com o mesmo nome.")
                input("\n")
            elif nome == "":
                print("Não é permitido criar uma tarefa sem nome.")
                input("\n")
            else:
                lista_tarefas.append(tarefa)

                escrever_json(arquivo_tarefas,lista_tarefas)

        elif opcao == "2":

            try: 
                ler_json(arquivo_tarefas)
                a = lista_tarefas[0]

            except FileNotFoundError:
                print("Nenhuma tafefa encontrada.")
                input("\n")
            except IndexError:
                print("Nenhuma tafefa encontrada.")
                input("\n")
            else:
                limpar_tela()
                print("Suas tarefas:")
                for i in ler_json(arquivo_tarefas):
                    if i["concluida"] == False:
                        estado = "Pendente"
                    else:
                        estado = "Concluida"
                    print(i["nome"],"-",f"[{estado}]")
                input("\n")


        elif opcao == "3":

            try: 
                ler_json(arquivo_tarefas) 
                a = lista_tarefas[0]
            
            except FileNotFoundError:
                print("Nenhuma tafefa encontrada.")
                input("\n")
            except IndexError:
                print("Nenhuma tafefa encontrada.")
                input("\n")
            else:
                limpar_tela()
                print("Escreva o nome da tarefa que deseja concluir:")
                concluir_tarefa = input()
                tarefa_encontrada = False
                for i in lista_tarefas:
                    if i["nome"] == concluir_tarefa:
                        i["concluida"] = True
                        tarefa_encontrada = True
                if tarefa_encontrada:

                    escrever_json(arquivo_tarefas,lista_tarefas)
                    
                    print("Tarefa marcada como concluida.")
                    input("\n")
                else:
                    print("Não foi possivel encontrar a tarefa.")
                    input("\n")

        elif opcao == "4":
            try: 
                ler_json(arquivo_tarefas)
                a =lista_tarefas[0]
                        
            except FileNotFoundError:
                print("Nenhuma tafefa encontrada.")
                input("\n")
            except IndexError:
                print("Nenhuma tafefa encontrada.")
                input("\n")
            else:
                limpar_tela()
                print("Escreva o nome da tarefa que deseja remover:")
                remover_tarefa = input()
                tarefa_removida = False
                contador = -1
                for i in lista_tarefas:
                    contador = contador + 1
                    if i["nome"] == remover_tarefa:
                        lista_tarefas.pop(contador)
                        tarefa_removida = True
                if tarefa_removida:
                    
                    escrever_json(arquivo_tarefas,lista_tarefas)
                                    
                    print("Tarefa removida.")
                    input("\n")
                else:
                    print("Não foi possivel encontrar a tarefa.")
                    input("\n")

        elif opcao == "5":
            break
        
        else:
            input("escolha uma opção valida.")
        
        limpar_tela()

if __name__ == "__main__":
    main()







import json

## Gerenciador de tarefas

def escrever_json(arquivo,objeto):

    with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(objeto,arquivo_json)

def ler_json(arquivo):
    
    with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
        return json.load(arquivo_json)

def limpar_tela():
    for i in range(100):
        print("")

def ler_lista(lista):
    contador = 1
    for i in lista:
        if i["concluida"] == False:
            estado_concluida = "[Pendente]*"
        else:
            estado_concluida = "[Concluida]"
        print(f"{contador} {estado_concluida} - {i["nome"]}")
        contador += 1
    return contador
def titulo():
    print("===== GERENCIADOR DE TAREFAS =====")
    print("")
    


def main():

    
    while True:

        arquivo_tarefas = "tarefas.json"
        
        try: lista_tarefas = ler_json(arquivo_tarefas)
        
        except FileNotFoundError:
            lista_tarefas = []
        except json.JSONDecodeError:
            print("ARQUIVO TAREFAS CORROMPIDO")
            break
        if lista_tarefas == []:
            lista_vazia = True
        else:
            lista_vazia = False
        limpar_tela()
        titulo()
        print("Suas tarefas:")
        print("")
        
        ler_lista(lista_tarefas)

        print("")
        print("1. Adicionar tarefa")
        print("2. Concluir tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        print("")
        print("Escolha uma opção:")

        

        opcao = input()
        limpar_tela()
        if opcao == "1":

            

            limpar_tela()

            titulo()

            print("Escreva o nome da tarefa:")
            print("")
            numero_tarefa = ler_lista(lista_tarefas)
            
            nome_tarefa = input(f"{numero_tarefa} [Pendente]* - ").strip()
            
            tarefa = {"nome":nome_tarefa,"concluida":False}
            
            if lista_tarefas.count({"nome":nome_tarefa,"concluida":True}) + lista_tarefas.count({"nome":nome_tarefa,"concluida":False}) > 0:
                print("Não é permitido criar mais de uma tarefa com o mesmo nome.")
                input("\n")
            elif nome_tarefa == "":
                print("Não é permitido criar uma tarefa sem nome.")
                input("\n")
            else:
                lista_tarefas.append(tarefa)

                escrever_json(arquivo_tarefas,lista_tarefas)

        elif opcao == "2":

            if lista_vazia:
                input("Você não possui nenhuma tarefa.")
                continue
            
            limpar_tela()
            titulo()
            print("Escolha o numero da tarefa que deseja concluir,")
            print("selecione uma ja concluida para a deixar pendente:")
            print("")
            ler_lista(lista_tarefas)
            
            tarefa_selecionada = input("\n")

            try: tarefa = lista_tarefas[int(tarefa_selecionada)-1]
            except:
                continue
            tarefa["concluida"] = not tarefa["concluida"]
            escrever_json(arquivo_tarefas,lista_tarefas)

        elif opcao == "3":

            if lista_vazia:
                input("Você não possui nenhuma tarefa.")
                continue
            
            limpar_tela()
            titulo()
            print("Escolha o numero da tarefa que deseja remover:")
            print("")
            ler_lista(lista_tarefas)
            
            tarefa_selecionada = input("\n")
            try: lista_tarefas.pop(int(tarefa_selecionada)-1)
            except:
                continue
            escrever_json(arquivo_tarefas,lista_tarefas)

        elif opcao == "4":
            break
        
        else:
            input("escolha uma opção valida.")
        
        limpar_tela()

if __name__ == "__main__":
    main()


    pass



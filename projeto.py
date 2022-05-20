from tabulate import tabulate
import random

class Usuario:
    def __init__(self):
        self.id = None
        self.nome = None
        self.email  = None
        self.telefone = None
        self.lista_usuarios = list()
        self.dados = dict()
        self.dic_nomes = dict()
        self.sublista = list()


def cadastrar(self):
    self.dados.clear()
    self.id = str(random.randint(1,9999))
    self.nome = input("Digite seu nome: ")
    self.email = input("Digite seu email: ")     
    self.telefone = input("Digite seu telefone: ")
    self.dados = {
        "Id": self.id,
        "Nome": self.nome,
        "Email": self.email,
        "Telefone": self.telefone,
        }
    self.lista_usuarios.append(self.dados.copy())
    print("Usuário cadastrado com sucesso!")


def consultar(self, id):
    self.sublista.clear()
    nao_tem=''
    for dic in self.lista_usuarios:
        if id == (dic ["Id"]):
            nao_tem=False
            self.sublista.append(dic)
            print("Aqui esta o resultado da busca: ")
            print(tabulate(self.sublista, headers="keys", tablefmt="grid"))
            break     
        else:
          nao_tem=True
    if nao_tem == True:
      print("Id não encontrado!")
        

def listar(self):
    self.sublista.clear()
    for item in self.lista_usuarios:
        self.dic_nomes = {
          'Id': item ["Id"],
          'Nome': item ["Nome"],
        }
        self.sublista.append(self.dic_nomes.copy())
    print("Aqui está a lista de nomes cadastrados: ")
    print(tabulate(self.sublista, headers="keys", tablefmt="grid"))


def deletar(self, id):
    nao_tem = ''
    for dic in self.lista_usuarios:
        if id == (dic ["Id"]):
            nao_tem=False
            idx = self.lista_usuarios.index(dic)
            del self.lista_usuarios[idx]
            break
            
        else:
          nao_tem = True
    if nao_tem == True:
      print("Id não encontrado!")


def alterar(self, id):
    self.sublista.clear()
    atualizado = {}
    nao_tem = ''
    encerrar = 1
    for dic in self.lista_usuarios:
        if id == (dic ["Id"]):
            nao_tem=False
            while encerrar == 1:
                alterar_dado = input("Qual dado você gostaria de alterar?(Digite 0 para encerrar a alteração): ").lower()
                if alterar_dado == "nome":
                    novo_nome = input("Digite o novo nome: ")
                    atualizado["Nome"] = novo_nome
                    dic.update(atualizado)
                    print("Nome atualizado com sucesso!")
                elif alterar_dado == "email":
                    novo_email = input("Digite o novo email: ")
                    atualizado["Email"] = novo_email
                    dic.update(atualizado)
                    print("E-mail atualizado com sucesso!")
                elif alterar_dado == "telefone":
                    novo_telefone = input("Digite o novo telefone: ")
                    atualizado["Telefone"] = novo_telefone
                    dic.update(atualizado)
                    print("Telefone atualizado com sucesso!")
                elif alterar_dado == '0':
                    encerrar = 0
                    self.sublista.append(dic.copy())
                    print("Seus dados atualizados: ")
                    print(tabulate(self.sublista, headers="keys", tablefmt="grid"))
                else:
                  print("Digite um paramêtro válido!")
            break            
        else:
            nao_tem = True
    if nao_tem == True:
      print("Id não encontrado!")
    

usuario = input("Digite qualquer coisa para continuar: ")
print(f"Bem-vindo!")
usuario = Usuario()
encerramento = 1
while encerramento == 1:
    print("0 Para sair do sistema \n1 Para cadastrar um usuário \n2 Para consultar um usuário pelo ID \n3 Para listar todos os nomes cadastrados \n4 Para deletar um usuário pelo ID \n5 Para alterar um dado de um usuário ID.")
    opcao = input("O que deseja fazer? ")
    if opcao == '0':
        encerramento = '1'
        print("Você escolheu sair. Fechando o programa...")
    elif opcao == '1':
        cadastrar(usuario)
    elif opcao == '2':
        pesquisa = (input("Digite o id: "))
        consultar(usuario, pesquisa)
    elif opcao == '3':
        listar(usuario)
    elif opcao == '4':
        pesquisa = (input("Digite o id do usuário a ser deletado: "))
        deletar(usuario, pesquisa)
    elif opcao == '5':
        pesquisa = input("Digite o id: ")
        alterar(usuario, pesquisa)
    else:
        print("Digite uma opção válida!!!")

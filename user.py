import os

class Conta:

  def __init__(self): # Recebe o nome e já cria a conta com ele
    pass

  def criar_conta(self):

    nome = str(input('Informe o nome no qual será cadastrado a conta: '))
    arquivo_path = os.path.join(os.path.dirname(__file__), 'contas_urubu') # Pega o caminho para o arquivo de contas

    with open(arquivo_path, 'a+') as arquivo: # Abre o arquivo com as contas cadastradas podendo edita-lo
      arquivo.seek(0) # Move o cursor para o inicío da primeira linha
      linhas = arquivo.readlines() 
      for i in range(0, len(linhas)): 
        if linhas[i][0:linhas[i].rfind(' ')] == nome:
          print('Essa conta já existe.')
          return self.criar_conta()
      else: 
        print('Conta cadastrada com sucesso')
        return arquivo.write(f'{nome} 100.00\n') # Adiciona uma nova conta

  def login(self):
    
    nome = input('Informe o nome da conta: ')
    arquivo_path = os.path.join(os.path.dirname(__file__), 'contas_urubu') # Caminho do arquivo das contas
    
    with open(arquivo_path, 'a+') as arquivo:
      arquivo.seek(0)
      linhas = arquivo.readlines()
      objetivo = 0
      id = -1
      for i in range(0, len(linhas)): 
          id += 1
          if linhas[i][0:linhas[i].rfind(' ')] == nome:
            saldo = linhas[i][len(nome) + 1: len(linhas[i]) - 1]
            return nome, saldo, id
          else:
            objetivo += 1
      if objetivo == len(linhas):
        print('Essa conta não existe')
        return 0

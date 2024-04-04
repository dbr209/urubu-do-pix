import datetime
from os import path

import registro

class Banco:

  def __init__(self, name, saldo, id_conta):
    self.name = name
    self.saldo = float(saldo)
    self.infos = None
    self.id = int(id_conta)
    self.registro = registro.Alterar_Registro()

  def historico(self):

    transacoes_path = path.join(path.dirname(__file__), 'transacoes')

    with open(transacoes_path, 'r') as arquivo:
        arquivo.seek(0) # Move o cursor para o inicío da primeira linha
        lines = arquivo.readlines()
        for i in range(0, len(lines)):
          primeiro = lines[i].rfind(' ')
          segundo = lines[i][:primeiro].rfind(' ')
          line = [lines[i][:segundo], lines[i][segundo + 1:primeiro], lines[i][primeiro + 1:len(lines[i]) - 1]]
          if line[0] == self.name:
            self.infos = line
            self.infos.append(i)
            print('=' * 10, 'Transação Em Andamento', '=' * 10)
            print(f'Valor depositado: {line[1]}\nData do deposito: {line[2]}')
            break
        else:
          print('*** Essa não contém transações em andamento')

  def investir(self): # Função para fazer a transação financeira

    arquivo_path = path.join(path.dirname(__file__), 'transacoes')

    while True:
      valor_str = str(input('Informe o valor que você deseja depositar: '))
      if valor_str.isdigit() == True:
        valor = float(valor_str)
        if valor <= self.saldo:
          self.saldo -= valor
          with open(arquivo_path, 'a+') as arquivo:
            arquivo.seek(0) # Move o cursor para o inicío da primeira linha
            arquivo.write(f'{self.name} {valor:.2f} {datetime.date.today()}\n')
          return self.registro.mudar_saldo(self.id, self.saldo, self.name)
        else:
          print('Saldo Inválido')
          return self.investir()
      else:
        print('Valor Inválido')
        return self.investir()
      
  def retirar_valor(self):
    duracao_transacao = datetime.date.today() - datetime.date.fromisoformat(self.infos[2])
    if duracao_transacao.days > 30:
      duracao_transacao = 30
    else:
      duracao_transacao = duracao_transacao.days
    if duracao_transacao == 0:
      return print('Tempo mínimo de 1 dia para retirada não correspondido')
    rendimento = float(self.infos[1]) * (duracao_transacao * 0.333333)
    self.saldo += rendimento
    self.saldo = float(f'{self.saldo:.2f}')
    self.registro.excluir_transacao(self.infos[3])
    return self.registro.mudar_saldo(self.id, self.saldo, self.name)
    
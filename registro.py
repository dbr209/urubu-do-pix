import os

class Alterar_Registro:

    def __init__(self):
        pass

    def mudar_saldo(self, id, saldo, nome):

        arquivo_path = os.path.join(os.path.dirname(__file__), 'contas_urubu') # Pega o caminho para o arquivo de contas

        with open(arquivo_path, 'a+') as arquivo: # Abre o arquivo com as contas cadastradas podendo edita-lo
            arquivo.seek(0) # Move o cursor para o inicío da primeira linha
            linhas = arquivo.readlines()
            linhas[id] = f'{nome} {saldo:.2f}'
            print(linhas)
            arquivo.truncate(0)
            print(arquivo.readline()) 
            for i in range(0, len(linhas)):
                if i == len(linhas) - 1:
                    arquivo.write(f'{linhas[i]}\n')
                else:
                    arquivo.write(f'{linhas[i]}')
        return 0

    def excluir_transacao(self, id):

        arquivo_path = os.path.join(os.path.dirname(__file__), 'transacoes')

        with open(arquivo_path, 'a+') as arquivo:
            arquivo.seek(0)
            linhas = arquivo.readlines()
            del(linhas[id])
            arquivo.truncate(0)
            for i in range(0, len(linhas)):
                if i == len(linhas) - 1:
                    arquivo.write(f'{linhas[i]}\n')
                else:
                    arquivo.write(f'{linhas[i]}')
        return 0
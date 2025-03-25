import pandas as pd # importa a biblioteca pandas
import matplotlib.pyplot as plt

class Microfones(): # Define a classe Microfones
    def __init__(self, modelo, transdutor, aplicacao, padrao_polar, frequencia): # define os parâmetros analisados
        self.modelo = modelo
        self.transdutor = transdutor
        self.aplicacao = aplicacao
        self.padrao_polar = padrao_polar
        self.frequencia = frequencia

    def showmic(self): # cria a função showmic
        print(f"Modelo: {self.modelo}")
        print(f"Transdutor: {self.transdutor}")
        print(f"Aplicação: {self.aplicacao}")
        print(f"Padrão Polar: {self.padrao_polar}")
        print(f"Frequência: {self.frequencia}")

def importar_excel(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)

    microfones = []

    for _, row in df.iterrows():
        microfone = Microfones(
            modelo=row["Modelo"],
            transdutor=row["Transdutor"],
            aplicacao=row["Aplicação"],
            padrao_polar=row["Padrão Polar"],
            frequencia=row["Frequência"]
        )
        microfones.append(microfone)

    return microfones

caminho_arquivo = r"C:\Users\eduardo\Downloads\Tabela Guia de Microfones Shure.xlsx"

microfones_lista = importar_excel(caminho_arquivo)

for microfone in microfones_lista:
    microfone.showmic() 

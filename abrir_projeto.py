#PROJETO ANCINE
#CLASSE PARA INICIAR PROJETO


class Projeto:
    
    def __init__(self) -> None:
        ...
    def abrir_projeto(self):
        import pandas as pd
        from processamento_dados import LeitorCSV
        from documentacao import Documentacao
        self.df = LeitorCSV()
        self.doc = Documentacao()
        self.df.leitura_csv_e_declaracao_variaveis_dados()
        self.df.padronizar_colunas()
        bem_vindo = """
***Bem vindo(a) ao Projeto!***

Para ler documentação: "pj.doc.documentacao"
"""
        print(bem_vindo)


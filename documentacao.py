#PROJETO ANCINE
#CLASSE PARA RETORNAR DOCUMENTAÇÂO

class Documentacao:

    def __init__(self) -> None:
        
        self.doc = None
    
    def documentacao(self):
        
        doc = f"""**** DOCUMENTAÇÃO DO PROJETO ****
***Agência Nacional do Cinema***

Cada Arquivo CSV contém uma variável raíz e um 
número de referência para variáveis específicas.
*
*
Para chamar variável no Jupyter Notebook digite: "df." + variável
*
Para chamar variável específica digite: "df." + "variável_especifica" + número
*
*
Nome arquivo CSV | Nome variável raíz | Número variável específica
-
Agentes Econômicos Regulares = agnts_economicos = 1  
Atividades Economicas dos Agentes Regulares = atividade_economicas_agnts = 2 
Projetos Renúncia Fiscal = proj_renuncia_fiscal = 3  
Obras não Publicitárias Brasileiras - Fomento Indireto = obras_n_publi_fomento_direto =  4 
Obras não Publcitárias Brasileiras - Investimento FSA = obras_n_publi_investimento_fsa =  5 
Processos de Prestação de contas = processos_prestacao_contas = 6  
Investidores de projetos de Renúncia Fiscal = investidores_proj_renuncia_fiscal = 7   
Produtoras Independentes = produtoras_independentes = 8 
Produtores de obra não Publicitárias Brasileiras = produtores_obras_n_publi = 9 
Projetos contratados - FSA e Desembolso = proj_fsa_desembolso = 10  
Relação de Grupos Econômicos = relacao_grupos_economicos = 11
Salas de Exibição e Complexos = salas_complexos = 12
*
*
Para exibir documentação de arquivo de dados, chamar função: documentacao_especifica()
argumento: variável raíz
**
Para exibir lista de funções úteis: indice_funcao()"""
        print(doc)

    def indice_funcao():

        funcoes = """
Função para buscar valores nulos: pj.df.achar_valores_nulos()"""



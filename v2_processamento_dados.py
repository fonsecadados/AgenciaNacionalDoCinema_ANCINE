
#PROJETO_ANCINE
#CLASSE PARA CARREGAMENTO E PRÉ PROCESSAMENTO DOS DADOS BRUTOS 
import pandas as pd
import pandas

"""Leitura dos dados brutos
df_agentes_economicos  
df_atividades_agentes_economicos  
df_projetos_renuncia_fiscal  
df_obras_nao_publicitaria_fomento_indireto  
df_obras_nao_publicitaria_investimento_fsa  
df_processos_em_prestação_de_contas  
df_investidores_projetos_renuncia_fiscal  
df_produtoras_independentes  
df_produtores_obras_nao_publicitarias_brasileiras  
df_projetos_contratados_fsa_desembolso  
df_projetos_renuncia_fiscal  
df_salas_e_complexos  
"""

class LeitorCSV:

    def __init__(self):
        self.__df_agentes_economicos = None
        self.__df_atividades_economicas_agentes = None
        self.__df_projetos_renuncia_fiscal = None
        self.__df_obras_nao_publicitaria_fomento_indireto = None
        self.__df_obras_nao_publicitaria_investimento_fsa = None
        self.__df_processos_em_prestacao_de_contas = None
        self.__df_investidores_projetos_renuncia_fiscal = None
        self.__df_produtoras_independentes = None
        self.__df_produtores_obras_nao_publicitarias_brasileiras = None
        self.__df_projetos_contratados_fsa_desembolso = None
        self.__df_relacao_grupos_economicos = None
        self.__df_salas_e_complexos = None

    def leitura_csv_e_declaracao_variaveis_dados(self):
        self.__df_agentes_economicos = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\AgentesEconomicosRegulares.csv', encoding='latin1', sep=';')
        self.agnts_economicos = pd.DataFrame(self.__df_agentes_economicos)
        #
        self.__df_atividades_economicas_agentes = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\AtividadesEconomicasAgentesRegulares.csv', encoding='latin1', sep=';')
        self.atividade_economicas_agnts = pd.DataFrame(self.__df_atividades_economicas_agentes)
        #
        self.__df_projetos_renuncia_fiscal = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\ProjetosRenunciaFiscal.csv', encoding='latin1', sep=';') 
        self.proj_renuncia_fiscal = pd.DataFrame(self.__df_projetos_renuncia_fiscal)
        #
        self.__df_obras_nao_publicitaria_fomento_indireto = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\ObrasNaoPubBrasileirasFomentoIndireto.csv', encoding='utf-16be', sep=';')
        self.obras_n_publi_fomento_direto = pd.DataFrame(self.__df_obras_nao_publicitaria_fomento_indireto)
        #
        self.__df_obras_nao_publicitaria_investimento_fsa = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\ObrasNaoPubBrasileirasInvestimentoFsa.csv', encoding='utf-16be', sep=';')
        self.obras_n_publi_investimento_fsa = pd.DataFrame(self.__df_obras_nao_publicitaria_investimento_fsa)
        #
        self.__df_processos_em_prestacao_de_contas = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\ProcessosEmPrestacaoDeContas.csv', encoding='latin1', sep=';')
        self.processos_prestacao_contas =  pd.DataFrame(self.__df_processos_em_prestacao_de_contas)
        #
        self.__df_investidores_projetos_renuncia_fiscal = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\InvestidoresEmProjetosRenunciaFiscal.csv', encoding='latin1', sep=';')
        self.investidores_proj_renuncia_fiscal = pd.DataFrame(self.__df_investidores_projetos_renuncia_fiscal)
        #
        self.__df_produtoras_independentes = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\ProdutorasIndependentes.csv', encoding='latin1', sep=';')
        self.produtoras_independentes = pd.DataFrame(self.__df_produtoras_independentes)
        #
        self.__df_produtores_obras_nao_publicitarias_brasileiras = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\ProdutoresDeObrasNaoPublicitariasBrasileiras.csv', encoding='latin1', sep=';')
        self.produtores_obras_n_publi =  pd.DataFrame(self.__df_produtores_obras_nao_publicitarias_brasileiras)
        #
        self.__df_projetos_contratados_fsa_desembolso = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\ProjetosContratadosFSAeDesembolso.csv', encoding='latin1', sep=';')
        self.proj_fsa_desembolso =  pd.DataFrame(self.__df_projetos_contratados_fsa_desembolso)
        #
        self.__df_relacao_grupos_economicos = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\RelacaoGruposEconomicos.csv', encoding='latin1', sep=';')
        self.relacao_grupos_economicos = pd.DataFrame(self.__df_relacao_grupos_economicos)
        #
        self.__df_salas_e_complexos = pd.read_csv('C:\\Users\\syafo\\OneDrive\\Documentos\\GitHub\\AgenciaNacionalDoCinema_ANCINE\\data\\SalasDeExibicaoEComplexos.csv', encoding='latin1', sep=';')
        self.salas_complexos = pd.DataFrame(self.__df_salas_e_complexos)
        
    def padronizar_colunas(self):
        #Agentes Econômicos - 1
        mapping_1 = {'SIM' : True, 'NÃO' : False}
        self.agnts_economicos['DATA_REGISTRO'] = pd.to_datetime(self.agnts_economicos['DATA_REGISTRO'], dayfirst=True)
        self.agnts_economicos['DATA_CONSTITUICAO'] = pd.to_datetime(self.agnts_economicos['DATA_CONSTITUICAO'], dayfirst=True)
        self.agnts_economicos['BRASILEIRO_INDEPENDENTE'] = self.agnts_economicos['BRASILEIRO_INDEPENDENTE'].map(mapping_1)
        #
        #Atividade Econômica Agentes - 2
        mapping_2 = { 'PRINCIPAL' : 1, 'SECUNDARIA' : 0}
        self.atividade_economicas_agnts['CLASSIFICACAO_ATIVIDADE'] = self.atividade_economicas_agnts['CLASSIFICACAO_ATIVIDADE'].map(mapping_2)
        #
        #ProjetosRenunciaFiscal - 3
        mapping_3 = {'DEFERIDO' : 1, 'IRREGULAR' : 0}
        self.proj_renuncia_fiscal['DT_1_LIBERACAO'] = pd.to_datetime(self.proj_renuncia_fiscal['DT_1_LIBERACAO'], dayfirst=True)
        self.proj_renuncia_fiscal['DT_APROVACAO_CAPTACAO'] = pd.to_datetime(self.proj_renuncia_fiscal['DT_APROVACAO_CAPTACAO'], dayfirst=True)
        self.proj_renuncia_fiscal['SITUACAO_REGISTRO'] = self.proj_renuncia_fiscal['SITUACAO_REGISTRO'].map(mapping_3)
        #
        #ObrasNaoPubBrasileirasFomentoIndireto - 4
        #SEM NECESSIDADE DE PADRONIZAR
        #
        #ObrasNaoPubBrasileirasInvestimentoFsa - 5
        #
        #ProcessosEmPrestacaoDeContas - 6
        #
        #InvestidoresEmProjetosRenunciaFiscal - 7
        #
        #ProdutorasIndependentes - 8
        #
        #ProdutoresDeObrasNaoPublicitariasBrasileiras - 9
        #
        #ProjetosContratadosFSAeDesembolso - 10
        #
        #RelacaoGruposEconomicos - 11
        #
        #SalasDeExibicaoEComplexos - 12

    def achar_valores_nulos(self, dado, coluna=1):
        import pandas as pd
        if dado:
            isnull = dado[dado.isnull().any(axis=1)]
            count = len(isnull)
            print(f"Quantidade de valroes Nulos:{count}")
        
        elif coluna != 1:
            isnull = dado[dado[coluna].isnull()]
            count = len(isnull)
            print(f"Quantidade de valroes Nulos:{count}")




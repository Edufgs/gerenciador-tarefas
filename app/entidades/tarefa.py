class Tarefa():
    #__init__ é um construtor
    def __init__(self, titulo, descricao, data_expiracao, prioridade, usuario):
        #__ é para dizer que é um atributo privado
        self.__titulo = titulo
        self.__descricao= descricao
        self.__data_expiracao = data_expiracao
        self.__prioridade = prioridade
        self.__usuario = usuario
        
    @property #Retorna o valor do atributo
    def titulo(self):
        return self.__titulo
    
    @titulo.setter #Define o valor do atributo
    def titulo(self,titulo):
        self.__titulo = titulo
        
    @property #Retorna o valor do atributo
    def descricao(self):
        return self.__descricao
    
    @descricao.setter #Define o valor do atributo
    def descricao(self,descricao):
        self.__descricao = descricao
        
    @property #Retorna o valor do atributo        
    def data_expiracao(self):
        return self.__data_expiracao
    
    @data_expiracao.setter #Define o valor do atributo
    def data_expiracao(self,data_expiracao):
        self.__data_expiracao = data_expiracao
        
    @property #Retorna o valor do atributo
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter #Define o valor do atributo
    def prioridade(self,prioridade):
        self.__prioridade = prioridade
        
    @property #Retorna o valor do atributo
    def usuario(self):
        return self.__usuario
    
    @usuario.setter #Define o valor do atributo
    def usuario(self,usuario):
        self.__prioridade = usuario
    
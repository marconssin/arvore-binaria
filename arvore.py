class Noh:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.esq = None  
        self.dir = None 

class Bst:
    def __init__(self, noh_raiz = None):
        self.raiz = noh_raiz
    
    def inserir (self, noh):
        if self.raiz is None:
            self.raiz = noh
        else:
            self._inserir_recursivo(self.raiz, noh)
    
    def _inserir_recursivo(self, atual, novo_noh):
        if novo_noh.idade < atual.idade:
            if atual.esq is None:
                atual.esq = novo_noh
            else:
                self._inserir_recursivo(atual.esq, novo_noh)
        else:
            if atual.dir is None:
                atual.dir = novo_noh
            else:
                self._inserir_recursivo(atual.dir, novo_noh)

            



#    def buscar (self, x):
#    def inOrder (self, x):
#    def preOrder (self, x):
#    def posOrder (self,x ):
#    def decOrder (sefl, x):
#    def largura (self, x):


print("Iniciando a árvore binária de busca...")

candidatos = [
    {"idade": 25, "nome": "pedro"},
    {"idade": 30, "nome": "marcos"},
    {"idade": 45, "nome": "marcelo"},
    {"idade": 18, "nome": "camila"},
    {"idade": 22, "nome": "scarlet"},
    {"idade": 35, "nome": "matheus"},
    {"idade": 20, "nome": "thiago"},
    {"idade": 65, "nome": "joaquim"},
    {"idade": 51, "nome": "michel"},
    {"idade": 43, "nome": "julia"},
]

arvore = Bst()
for candidato in candidatos:
    noh = Noh(candidato["nome"], candidato["idade"])
    arvore.inserir(noh)


print(arvore.raiz.nome)
print(arvore.raiz.esq.nome)
print(arvore.raiz.dir.nome)

arvore_2 = Bst()

arvore_2  = arvore.raiz.esq
print(arvore_2.nome)




    


#print(candidatos[0])
#print(candidatos[1])
#print(candidatos[2])
#print(candidatos[3])
#print(candidatos[4])
#print(candidatos[5])
#print(candidatos[6])
#print(candidatos[7])
#print(candidatos[8])
#print(candidatos[9])


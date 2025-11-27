class Noh:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.esq = None  
        self.dir = None 

class Bst:
    def __init__(self, noh_raiz = None):
        self.raiz = noh_raiz
    
#    def inserir (self, x):
#    def buscar (self, x):
#    def inOrder (self, x):
#    def preOrder (self, x):
#    def posOrder (self,x ):
#    def decOrder (sefl, x):
#    def largura (self, x):


print("Iniciando a árvore binária de busca...")

candidatos = [
    {"idade": 30, "nome": "pedro"},
    {"idade": 25, "nome": "marcos"},
    {"idade": 45, "nome": "marcelo"},
    {"idade": 18, "nome": "camila"},
    {"idade": 22, "nome": "scarlet"},
    {"idade": 35, "nome": "matheus"},
    {"idade": 20, "nome": "thiago"},
    {"idade": 65, "nome": "joaquim"},
    {"idade": 51, "nome": "michel"},
    {"idade": 43, "nome": "julia"},
]

print(candidatos[0])
print(candidatos[1])
print(candidatos[2])
print(candidatos[3])
print(candidatos[4])
print(candidatos[5])
print(candidatos[6])
print(candidatos[7])
print(candidatos[8])
print(candidatos[9])


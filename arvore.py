#Implementação das classes

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
            if novo_noh.idade > atual.idade:
                if atual.dir is None:
                    atual.dir = novo_noh
                else:
                    self._inserir_recursivo(atual.dir, novo_noh)
            else:
                if novo_noh.nome < atual.nome:
                    if atual.esq is None:
                        atual.esq = novo_noh
                    else:
                        self._inserir_recursivo(atual.esq, novo_noh)
                else:
                    if atual.dir is None:
                        atual.dir = novo_noh
                    else:
                        self._inserir_recursivo(atual.dir, novo_noh)

    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}") 
            self.inOrder(atual.dir)
  
    def preOrder(self, atual):
        if atual != None:
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")
            self.preOrder(atual.esq)
            self.preOrder(atual.dir)
       
    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esq)
            self.posOrder(atual.dir)
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")

    def decOrder(self, atual):
        if atual != None:
            self.decOrder(atual.dir)
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")
            self.decOrder(atual.esq)

    def largura(self, atual):
        if atual != None:
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")
            self.largura(atual.esq)
            self.largura(atual.dir)

# Fim da implementação das classes

# Início do fluxo principal

#Populando uma lista de dicionários para usar como dados de entrada
candidatos = [
    {"idade": 25, "nome": "pedro"},
    {"idade": 30, "nome": "marcos"},
    {"idade": 45, "nome": "marcelo"},
    {"idade": 18, "nome": "scarlet"},
    {"idade": 18, "nome": "camila"},
    {"idade": 35, "nome": "matheus"},
    {"idade": 20, "nome": "thiago"},
    {"idade": 65, "nome": "joaquim"},
    {"idade": 51, "nome": "michel"},
    {"idade": 43, "nome": "julia"},
]

#Criando a árvore binária e populando com a lista criada anteriormente
arvore = Bst()
for candidato in candidatos:
    noh = Noh(candidato["nome"].lower(), candidato["idade"])
    arvore.inserir(noh)

no_raiz = arvore.raiz

#Navegando na árvore binária criada
print("In Order:")
arvore.inOrder(no_raiz)
print()
print("Pre Order:")
arvore.preOrder(no_raiz)
print()
print("Pos Order:")
arvore.posOrder(no_raiz)
print()
print("Dec Order:")
arvore.decOrder(no_raiz)
print()
print("Largura:")
arvore.largura(no_raiz)
print()
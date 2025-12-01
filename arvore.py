# arvore.py
# Implementação das classes

# Classe que implementa um nó na árvore binária de busca (bst)
class Noh:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.esq = None  
        self.dir = None 

# Classe que implementa a árvore binária de busca (bst)
class Bst:
    def __init__(self, noh_raiz = None):
        self.raiz = noh_raiz
    
    def inserir(self, noh):
        if self.raiz is None:
            self.raiz = noh
        else:
            self._inserir_arvore(self.raiz, noh)
    
    def _inserir_arvore(self, atual, novo_noh):
        if novo_noh.idade < atual.idade:
            if atual.esq is None:
                atual.esq = novo_noh
            else:
                self._inserir_arvore(atual.esq, novo_noh)
        else:
            if novo_noh.idade > atual.idade:
                if atual.dir is None:
                    atual.dir = novo_noh
                else:
                    self._inserir_arvore(atual.dir, novo_noh)
            else:
                if novo_noh.nome < atual.nome:
                    if atual.esq is None:
                        atual.esq = novo_noh
                    else:
                        self._inserir_arvore(atual.esq, novo_noh)
                else:
                    if atual.dir is None:
                        atual.dir = novo_noh
                    else:
                        self._inserir_arvore(atual.dir, novo_noh)

    def em_ordem(self, atual):
        if atual != None:
            self.em_ordem(atual.esq)
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}") 
            self.em_ordem(atual.dir)
  
    def pre_ordem(self, atual):
        if atual != None:
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")
            self.pre_ordem(atual.esq)
            self.pre_ordem(atual.dir)
       
    def pos_ordem(self, atual):
        if atual != None:
            self.pos_ordem(atual.esq)
            self.pos_ordem(atual.dir)
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")

    def dec_ordem(self, atual):
        if atual != None:
            self.dec_ordem(atual.dir)
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")
            self.dec_ordem(atual.esq)

    def em_largura(self, atual):
        if atual is None:
            return
        fila = []
        fila.append(atual)
        while len(fila) > 0:
            atual = fila.pop(0)
            print(f"Nome: {atual.nome.ljust(10)} - Idade: {atual.idade}")
            if atual.esq is not None:
                fila.append(atual.esq)
            if atual.dir is not None:
                fila.append(atual.dir)        

# Fim da implementação das classes

# Início do fluxo principal

# Populando uma lista de dicionários para usar como dados de entrada
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

# Criando a árvore binária e populando com a lista criada anteriormente
arvore = Bst()
for candidato in candidatos:
    noh = Noh(candidato["nome"].lower(), candidato["idade"])
    arvore.inserir(noh)

# Navegando na árvore binária criada
print()
print("In Order:")
arvore.em_ordem(arvore.raiz)
print()
print("Pre Order:")
arvore.pre_ordem(arvore.raiz)
print()
print("Pos Order:")
arvore.pos_ordem(arvore.raiz)
print()
print("Dec Order:")
arvore.dec_ordem(arvore.raiz)
print()
print("Largura:")
arvore.em_largura(arvore.raiz)
print()
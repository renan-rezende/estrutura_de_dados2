class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def imprimir_caminhos_folha_ate_raiz(raiz):
    if raiz is None:
        return

    # Pilha vai guardar pares: (nó_atual, caminho_até_aquele_nó)
    pilha = []
    pilha.append((raiz, []))

    while pilha:
        no, caminho = pilha.pop()
        novo_caminho = caminho + [no.valor]

        # Se for folha, imprime o caminho da folha até a raiz
        if no.esquerda is None and no.direita is None:
            print(" -> ".join(map(str, reversed(novo_caminho))))
        else:
            # Adiciona os filhos na pilha
            if no.esquerda:
                pilha.append((no.esquerda, novo_caminho))
            if no.direita:
                pilha.append((no.direita, novo_caminho))

# Criando a árvore
raiz = Node(1)
raiz.esquerda = Node(2)
raiz.direita = Node(3)
raiz.esquerda.esquerda = Node(4)
raiz.esquerda.direita = Node(5)
raiz.direita.esquerda = Node(6)
raiz.direita.direita = Node(7)
raiz.direita.esquerda.esquerda = Node(8)
raiz.direita.esquerda.direita = Node(9)

# Executar função
imprimir_caminhos_folha_ate_raiz(raiz)

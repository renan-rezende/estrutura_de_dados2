class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def arvores_identicas(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.valor != b.valor:
        return False
    return (arvores_identicas(a.esquerda, b.esquerda) and
            arvores_identicas(a.direita, b.direita))

# Montagem da arvore1
arvore1 = Node(1)
arvore1.esquerda = Node(2)
arvore1.direita = Node(3)
arvore1.esquerda.esquerda = Node(4)
arvore1.esquerda.direita = Node(5)
arvore1.direita.esquerda = Node(6)
arvore1.direita.direita = Node(7)

# Montagem da arvore2
arvore2 = Node(1)
arvore2.esquerda = Node(2)
arvore2.direita = Node(3)
arvore2.esquerda.esquerda = Node(4)
arvore2.esquerda.direita = Node(5)
arvore2.direita.esquerda = Node(6)
arvore2.direita.direita = Node(7)

# Verificação
resultado = arvores_identicas(arvore1, arvore2)
print(resultado)  # Saída: True

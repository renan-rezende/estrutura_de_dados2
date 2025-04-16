class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def preorder(raiz):
    if raiz:
        print(raiz.valor, end=" ")
        preorder(raiz.esquerda)
        preorder(raiz.direita)

def inorder(raiz):
    if raiz:
        inorder(raiz.esquerda)
        print(raiz.valor, end=" ")
        inorder(raiz.direita)

def postorder(raiz):
    if raiz:
        postorder(raiz.esquerda)
        postorder(raiz.direita)
        print(raiz.valor, end=" ")

# Montar a árvore
raiz = Node(1)
raiz.esquerda = Node(2)
raiz.direita = Node(3)
raiz.esquerda.esquerda = Node(4)
raiz.direita.esquerda = Node(5)
raiz.direita.direita = Node(6)
raiz.direita.esquerda.esquerda = Node(7)
raiz.direita.esquerda.direita = Node(8)

# Testando as travessias
print("Preorder:")
preorder(raiz)

print("\nInorder:")
inorder(raiz)

print("\nPostorder:")
postorder(raiz)

C:\Users\alunolab12\teste\atividade1.py
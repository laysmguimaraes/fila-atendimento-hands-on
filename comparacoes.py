import heapq
import random

# Parte 1 - Fila FIFO

class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, cliente):
        self.itens.append(cliente)

    def dequeue(self):
        if not self.empty():
            return self.itens.pop(0)
        return None

    def head(self):
        if not self.empty():
            return self.itens[0]
        return None

    def size(self):
        return len(self.itens)

    def empty(self):
        return len(self.itens) == 0


# Parte 2 - Fila Circular

class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.front = 0
        self.rear = 0
        self.total = 0

    def _formatar_fila(self):
        clientes = []
        for indice in range(self.total):
            posicao = (self.front + indice) % self.capacidade
            cliente = self.fila[posicao]
            clientes.append(f"{cliente['nome']} (senha {cliente['senha']})")
        return " -> ".join(clientes) if clientes else "vazia"

    def enqueue(self, cliente):
        if self.total == self.capacidade:
            print(f"Não foi possível inserir {cliente['nome']}.")
            return False

        self.fila[self.rear] = cliente
        self.rear = (self.rear + 1) % self.capacidade
        self.total += 1
        print(f"Inserido: {cliente['nome']} | Front: {self.front} | Rear: {self.rear} | Fila: {self._formatar_fila()}")
        return True

    def dequeue(self):
        if self.total == 0:
            print(" Fila Vazia!")
            return None

        cliente = self.fila[self.front]
        self.fila[self.front] = None  # Limpa 
        self.front = (self.front + 1) % self.capacidade
        self.total -= 1
        print(f"Atendido: {cliente['nome']} | Front: {self.front} | Rear: {self.rear} | Fila: {self._formatar_fila()}")
        return cliente


# Parte 3 - Fila de Prioridade

class FilaPrioridade:
    def __init__(self):
        self.heap = []
        self.contador = 0
    def enqueue(self, cliente):
        heapq.heappush(self.heap, (cliente["prioridade"], self.contador, cliente))
        self.contador += 1

    def dequeue(self):
        if self.heap:
            prioridade, ordem, cliente = heapq.heappop(self.heap)
            return cliente
        return None

    def empty(self):
        return len(self.heap) == 0


#Teste

print("=== Teste Fila FIFO (10 Clientes) ===")
fila_classica = Fila()
for i in range(1, 11):
    c = {"nome": f"Cliente_{i}", "senha": i, "prioridade": random.randint(1, 3)}
    fila_classica.enqueue(c)

print(f"Total na fila: {fila_classica.size()}")
print("Atendendo em ordem FIFO:")
while not fila_classica.empty():
    atendido = fila_classica.dequeue()
    print(f"Atendendo: {atendido['nome']} (Senha: {atendido['senha']})")

print("\n=== Fila Circular ===")
fc = FilaCircular(5)
# Inserindo 5 clientes
for i in range(1, 6):
    fc.enqueue({"nome": f"Cli_{i}", "senha": i, "prioridade": 3})

# Removendo 2 clientes 
print("\n-- Removendo 2 clientes --")
fc.dequeue()
fc.dequeue()

# Inserindo mais 2 
print("\n-- Reutilizando posições liberadas --")
fc.enqueue({"nome": "Cli_6", "senha": 6, "prioridade": 3})
fc.enqueue({"nome": "Cli_7", "senha": 7, "prioridade": 3})


print("\n=== Desafio final ===")
# 1. Gerar 20 clientes
clientes_desafio = []
for i in range(1, 21):
    clientes_desafio.append({
        "nome": f"Pessoa_{i}",
        "senha": i,
        "prioridade": random.randint(1, 3)
    })

print("\n1. Clientes gerados (Ordem de Chegada):")
for c in clientes_desafio:
    print(f"Senha: {c['senha']:02d} | Nome: {c['nome']} | Prioridade: {c['prioridade']}")

# 2. Atendimento Fila Clássica
print("\n2. Atendimento na Fila Clássica (FIFO):")
f_simples = Fila()
for c in clientes_desafio:
    f_simples.enqueue(c)
while not f_simples.empty():
    c = f_simples.dequeue()
    print(f"Chamando {c['nome']} - Senha {c['senha']}")

# 3. Fila de Prioridade
print("\n3. Atendimento na Fila de Prioridade (1=Emergência, 2=Prioritário, 3=Normal):")
f_prio = FilaPrioridade()
for c in clientes_desafio:
    f_prio.enqueue(c)
while not f_prio.empty():
    c = f_prio.dequeue()
    print(f"Chamando {c['nome']} (Prioridade {c['prioridade']}, Senha {c['senha']})")
    
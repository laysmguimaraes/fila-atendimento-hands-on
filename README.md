# Sistema Inteligente de Atendimento (`fila-atendimento-hands-on`)
---

## Descrição do Projeto
Este projeto simula uma central de atendimento utilizando três estruturas de dados diferentes em Python:
* **Fila Clássica (FIFO):** Quem chega primeiro é atendido primeiro[cite: 1].
* **Fila Circular:** Fila com limite de lugares que reaproveita os espaços vazios[cite: 1, 3].
* **Fila de Prioridade:** Quem tem maior urgência é atendido à frente, mesmo que tenha chegado mais tarde[cite: 1, 3].

---

## Análise

1. Por que a ordem de atendimento da fila de prioridade pode ser diferente da ordem da fila clássica?<br>
Na fila clássica, a regra é FIFO (First In, First Out) quem chega primeiro é sempre atendido primeiro, ja na fila de prioridade, a regra principal é a gravidade da situação, se uma pessoa com prioridade 1 (Emergência) chegar mais tarde, ela passa na frente de quem tem prioridade 3 (Normal), mesmo que a outra pessoa já estivesse esperando há mais tempo

2. Em quais situações reais uma fila de prioridade seria mais adequada?<br>
-Pronto-socorro e hospitais, pacientes com risco de vida precisam de atendimento imediato, enquanto casos leves podem esperar
-Processos em sistemas operacionais, interrupções de hardware/críticas antes de tarefas de fundo

3. Quais são as vantagens e limitações de uma fila circular?<br>
Vantagens- ocupa um tamanho fixo de memória e reutiliza as posições liberadas logo no início da lista assim que sai, sem mover os outros elementos 
Limitações- o tamanho é limitado, se a fila encher e não sair ninguém, ela não aceita mais pessoas até seja liberado um lugar

4. O que acontece ao tentar inserir um elemento em uma fila circular cheia?<br>
Acontece um erro chamado estouro de fila ou Queue Overflow, o sistema não tem onde guardar o novo dado e precisa de recusar para não apagar nem misturar os dados de quem já estava na fila

## Como Executar o Código
1. Certifique-se de que tem o Python instalado no computador.
2. Abra o terminal na pasta do projeto e execute:
```bash
python main.py
Trabalho Sistemas Banco de Dados
================================
Escalonamento de Transações
===========================

Alunos:
~~~~~~~
- Gabriel de Souza Barreto
- Guilherme Bastos de Oliveira
~~~~~~~~~~~~~~~~~~~
Detecção de ciclos:

Para detectar os ciclos foi utilizado o algorito de Busca em Profundidade, implementado de maneira recursiva no método **Transacao.detectaCiclo()**.

Cada objeto **Transacao** é considerado um vértice, e a cada operação realizada é adicionado o arco se necessário.

Teste de equivalência:
~~~~~~~~~~~~~~~~~~~~~~
Quando todas as transações estão prontas, é procurado uma visão que seja equivalente.

Para cada visão, é testado se alguma das transações contém algum conflito. 
Caso todas as transações sejam equivalentes uma visão foi encontrada é o escalonamento é equivalente.

.. Trabalho BD documentation master file, created by
   sphinx-quickstart on Mon Nov 19 11:02:20 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Escalonamento de Transações
===========================

Alunos:
~~~~~~~
- Gabriel de Souza Barreto
- Guilherme Bastos de Oliveira

Detecção de ciclos:
~~~~~~~~~~~~~~~~~~~
Para detectar os ciclos foi utilizado o algorito de Busca em Profundidade, implementado de maneira recursiva no método **Transacao.detectaCiclo()**.

Cada objeto **Transacao** é considerado um vértice, e a cada operação realizada é adicionado o arco se necessário.

Teste de equivalência:
~~~~~~~~~~~~~~~~~~~~~~
Quando todas as transações estão prontas, é procurado uma visão que seja equivalente.

Para cada visão, é testado se alguma das transações contém algum conflito, caso todas as transações sejam equivalentes uma visão foi encontrada é o escalonamento é equivalente.

Código:
~~~~~~~

Documentação da classe Transacao:
---------------------------------
.. automodule:: Transacao
    :members:

Código Fonte:
-------------

.. toctree::
    :maxdepth: 3

    codigo.rst

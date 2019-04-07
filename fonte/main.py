#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from Transacao import Transacao
import itertools, sys

id_escalonamento = 1
transacoes = {}

def equivaleSerial(transacoes):
    equivale = True
    # para todo permutação
    for serial in itertools.permutations(transacoes.values()):
        equivale = True
        # para todas as transações
        for valor in transacoes.values():
            # se não equivale a visão
            if valor.naoEquivale(serial):
                equivale = False
        if equivale:
            return True
    return False

# para todas as linhas da entrada
for linha in sys.stdin:
    # lê a linha
    tempo, id, op, atributo = linha.upper().split()
    id = int(id)

    # se transação ainda não existe
    if id not in transacoes:
        transacoes[id] = Transacao(id, transacoes)
    # processa a operação
    transacoes[id].realiza(int(tempo), op, atributo)

    # verifica se todas as transações deram commit
    todas = map(lambda x: x.pronta, transacoes.values())
    todas = reduce(lambda x,y: x and y, todas)

    # se todas estão prontas
    if todas:
        resultado = "SS"
        # busca ciclo
        for t in transacoes.values():
            if t.estado == 0:
                if t.detectaCiclo():
                    resultado = "NS"
                    break

        # se equivale a alguma visão
        resultado += " SV" if equivaleSerial(transacoes) else " NV"

        # monta a saída
        chaves = transacoes.keys()
        chaves.sort()
        chaves = map(lambda x: str(x), chaves)
        print (str(id_escalonamento) + " " + ",".join(chaves) + " " + resultado)

        # prepara para próximo escalonamento
        id_escalonamento += 1
        transacoes = {}

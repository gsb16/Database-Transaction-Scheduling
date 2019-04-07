# -*- coding: utf-8 -*-

class Transacao:
	"""Classe que representa uma transação, armazena as operações e relações do grafo."""
	def __init__(self, id, escalonamento):
		# o escalonamento a que essa transação pertence
		self.escalonamento = escalonamento
		# se já realizou commit
		self.pronta = False
		# vizinhos no grafo
		self.vizinhos = []
		# operações realizadas
		self.acoes = {}
		# estado para busca de ciclos
		self.estado = 0
		# possíveis operações
		self.operacoes = {
			"R": self.ler,
			"W": self.escrever,
			"C": self.commit
		}
		# id da transação
		self.id = id

	def adicionaVizinho(self, vizinho):
		"""Se vizinho ainda não é vizinho de self, adiciona vizinho na em self.vizinhos"""
		# se já não é vizinho
		if vizinho not in self.vizinhos:
			self.vizinhos.append(vizinho)

	def detectaCiclo(self):
		"""Método recursiva para encontrar ciclo no grafo"""
		# se é vizinho de nodo já visitado, tem ciclo
		if self.estado == 1:
			return True

		self.estado = 1
		resultado = False
		# verifica se algum vizinho detecta ciclo
		for v in self.vizinhos:
			if v.estado != 2:
				resultado = resultado or v.detectaCiclo()
		self.estado = 2
		return resultado

	def escrever(self, acao, atributo):
		"""Método para tratar operação de escrita (W)"""
		# para toda transação t
		for t in self.escalonamento.values():
			# se não for ela
			if t != self:
				w = t.indexAcao("W", atributo)
				r = t.indexAcao("R", atributo)
				# se transação t escreve ou lê atributo antes
				if (w != -1 and w < acao) or (r != -1 and r < acao):
					# print (self.id, acao, atributo, w, r, t.id)
					t.adicionaVizinho(self)

	def ler(self, acao, atributo):
		"""Método para tratar operação de leitura (R)"""
		# para toda transação t
		for t in self.escalonamento.values():
			# se não for ela
			if t != self:
				index_w = t.indexAcao("W", atributo)
				# se transação t escreve no atributo antes
				if (index_w != -1 and index_w < acao):
					t.adicionaVizinho(self)

	def commit(self, tempo, atributo):
		"""Método para tratar operação de commit (C)"""
		self.pronta = True

	def realiza(self, tempo, op, atributo):
		"""Faz o processamento necessário para adicionar a operação op"""
		# adiciona a operação nas ações
		self.acoes[tempo] = (op, atributo)
		# executa a operação correspondente
		self.operacoes[op](tempo, atributo)

	def naoEquivale(self, serial):
		"""Verifica se self pode ser equivalente ao escalonamento serial"""
		# para todas as ações
		for acao, (op, atr) in self.acoes.iteritems():
			# se for leitura
			if op == "R":
				# filtra transações com operação de escrita no atributo antes e ordena
				tp = filter(lambda x: x.indexAcao("W", atr) != -1, self.escalonamento.values())
				tp = filter(lambda x: x.indexAcao("W", atr) < acao, tp)
				tp.sort(lambda x,y: x.indexAcao("W", atr) - y.indexAcao("W", atr))
				# pega a última transação com escrita em atr
				transacao_p = False
				if len(tp) > 0:
					transacao_p = tp[-1]
				# filtra da visão todas as ações que escrevem em atr
				ts = filter(lambda x: x.indexAcao("W", atr) != -1, serial[:serial.index(self)])
				# pega a última transação com escrita em atr
				transacao_s = False
				if len(ts) > 0:
					transacao_s = ts[-1]
				# se existe escrita antes no escalonamento e é diferente do serial
				if (transacao_p != transacao_s):
					return True

			# se for escrita
			if op == "W":
				# filtra transações com operação de escrita no atributo antes e ordena
				tp = filter(lambda x: x.indexAcao("W", atr) != -1, self.escalonamento.values())
				tp = filter(lambda x: x.indexAcao("W", atr) > acao, tp)

				# se é o último a escrever
				if len(tp) == 0:
					# para todas as transações seriais após
					for t in serial[serial.index(self)+1:]:
						# se escrever no atributo
						if t.indexAcao("W", atr) != -1:
							return True
		return False

	def indexAcao(self, op, atr):
		"""Retorna o primeiro indíce em que é feita uma operação do tipo op no atributo atr"""
		# para toda ação
		for chave, valor in self.acoes.iteritems():
			# se operação e atributo correspondem
			if valor == (op, atr):
				return chave
		return -1

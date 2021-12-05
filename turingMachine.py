"""
A classe MTU, Maquina de turing Universal com heuristica de deteccao de loop
"""

from collections import defaultdict

class MTU:
    # construtor da classe MTU
    def __init__( self, alphabet_symbols, blank, input_symbols, states, initial_state, transitions, tape):
        self.alphabet_symbols = alphabet_symbols
        self.blank = blank
        self.input_symbols = input_symbols
        self.states = states
        self.initial_state = initial_state
        # halt_states sao estados de parada, ou seja: que nao possuem transicoes para nenhum outro estado. Se a maquina para
        # em um halt_state a entrada e considerada aceita.
        self.halt_states = [x for x in states if x not in [x for x, y in transitions.keys()]] 
        self.transitions = transitions

        self.head = 0
        self.tape = defaultdict(lambda: self.blank, tape)
        self.current_state = 1
        self.halted = False
        
        
        self.per_config_count = dict.fromkeys(transitions.keys(), 0)
        self.total_config_count = 0
        self.config_limit = len(states)*len(tape.keys())
        
    # metodo imprime o estado atual e a fita com um span de 8 elementos da cabeca de leitura representada por 'v'
    def print(self, span=8):
        print(f'{"_" * (4 * span + 15)}')
        print(f'Estado atual = q{self.current_state-1}')
        print(f'{" " * (2 * span + 10)}v')
        print('Fita: ... ', end='')
        print(' '.join(chr(96 + self.tape[i]) if self.tape[i] != self.blank else 'B' for i in range(self.head - span, self.head + span + 1)), end='')
        print(' ...', end='\n')
    
    # metodo retorna resultado da maquina para a entrada (Aceita/Rejeitada)
    def result(self):
        if self.halted:
            if self.current_state in self.halt_states:
                return "Entrada Aceita!"
            else:
                return "Entrada Rejeitada!"
        else:
            return "Ainda em Execução!"

    def move_tape_head(self, direction):
        if direction == 1:
            self.head += 1
        elif direction == 2:
            self.head += -1

    def tape_write(self, symbol):
        self.tape[self.head] = symbol

    # metodo que aplica a heuristica implementada, chamado a cada passo da maquina,
    # retornando se o limite de configuracoes pre-estabelecido foi ultrapassado.
    def verify_loop(self):
        self.per_config_count[self.current_state, self.tape[self.head] if self.head < len(self.tape) else self.blank] += 1
        self.total_config_count += 1
        if self.per_config_count[self.current_state, self.tape[self.head] if self.head < len(self.tape) else self.blank] > self.config_limit:
            return True
        else:
            return False

    # metodo que executa os passos da maquina, até que a mesma pare.
    def step(self):
        if self.halted:
            raise RuntimeError('Maquina está parada.')
        try:
            # tenta transicao partindo do estado atual, lendo o elemento da fita onde a cabeca de leitura esta
            new_state, new_symbol, direction = self.transitions[self.current_state, self.tape[self.head] if self.head < len(self.tape) else self.blank]
            
            # heuristica para detectar loop.
            if self.verify_loop():
                continuar = input(f"Mais de {self.config_limit} da mesma configuração, máquina pode estar em loop.\nDeseja continuar? (sim/nao): ")
                if continuar == "sim":
                    self.config_limit *= 2
                elif continuar == "nao":
                    self.halted = True
                    raise RuntimeError(f'\n A máquina foi parada por loop detectado após {self.total_config_count} configurações.')

        except KeyError: # KeyError indica que o estado atual nao tem transicao para atual elemento, maquina para.
            self.halted = True
            return
        except RuntimeError as e: #RuntimeError indica que execucao foi finalizada pela heuristica, Erro relancado para main
            raise e
        
        # novo simbolo escrito na fita
        self.tape_write(new_symbol)
        # atualiza estado atual
        self.current_state = new_state
        # move a cabeca da fita na direcao da transicao
        self.move_tape_head(direction)

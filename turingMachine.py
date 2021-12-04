from collections import defaultdict
class MT:
   
    def __init__( self, alphabet_symbols, blank, input_symbols, states, initial_state, transitions, tape):
        self.alphabet_symbols = alphabet_symbols
        self.blank = blank
        self.input_symbols = input_symbols
        self.states = states
        self.initial_state = initial_state
        self.transitions = transitions

        self.head = 0
        self.tape = defaultdict(lambda: self.blank, tape)
        self.current_state = 1
        self.halted = False
        
        self.heuristicConfigCount = dict.fromkeys(transitions.keys(), 0)
        self.totalConfig = 0
        self.limitConfigurations = 500


    def print(self, span=10):
        print(f'{"_" * (4 * span + 15)}')
        print(f'Estado atual = q{self.current_state-1}')
        print(f'{" " * (2 * span + 10)}v')
        print('Fita: ... ', end='')
        print(' '.join(chr(96 + self.tape[i]) if self.tape[i] != self.blank else 'B' for i in range(self.head - span, self.head + span + 1)), end='')
        print(' ...', end='\n')
    

    def verify_loop(self):
        self.heuristicConfigCount[self.current_state, self.tape[self.head] if self.head < len(self.tape) else self.blank] += 1
        self.totalConfig += 1
        if self.heuristicConfigCount[self.current_state, self.tape[self.head] if self.head < len(self.tape) else self.blank] > self.limitConfigurations:
            return True
        else:
            return False

    def step(self):
        if self.halted:
            raise RuntimeError('Maquina está parada.')
        try:
            new_state, new_symbol, direction = self.transitions[self.current_state, self.tape[self.head] if self.head < len(self.tape) else self.blank]
            
            if self.verify_loop():
                continuar = input(f"Mais de {self.limitConfigurations} da mesma configuração, máquina pode estar em loop.\n Deseja continuar? (sim/nao) ")
                if continuar == "sim":
                    self.limitConfigurations *= 2
                elif continuar == "nao":
                    self.halted = True
                    return
        
        except KeyError:
            self.halted = True
            return
        self.tape[self.head] = new_symbol
        self.current_state = new_state
        if direction == 1:
            self.head += 1
        elif direction == 2:
            self.head += -1

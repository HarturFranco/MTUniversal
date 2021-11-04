class MT:
   
    def __init__( self, alphabet_symbols, blank, input_symbols, states, initial_state, transitions, tape):
        self.alphabet_symbols = alphabet_symbols
        self.blank = blank
        self.input_symbols = input_symbols
        self.states = states
        self.initial_state = initial_state
        self.transitions = transitions

        self.head = 0
        self.tape = tape
        self.current_state = 1
        self.halted = False

    def print_state(self):
        simbolo_atual = self.tape[self.head] if self.head < len(self.tape) else self.blank
        print("(" + str(self.current_state) + ',' + str(simbolo_atual) + ")")
        try:
            print(self.transitions[self.current_state, simbolo_atual])
        except KeyError:
            print("Sem transição")

    def step(self):
        if self.halted:
            raise RuntimeError('Maquina está parada.')
        try:
            new_state, new_symbol, direction = self.transitions[self.current_state, self.tape[self.head] if self.head < len(self.tape) else self.blank]
        except KeyError:
            self.halted = True
            return
        self.tape[self.head] = new_symbol
        self.current_state = new_state
        if direction == 1:
            self.head += 1
        elif direction == 2:
            self.head += -1

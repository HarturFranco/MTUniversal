from turingMachine import MT


# Decodificador:
# turing machine
def decode_UTM_text():
    with open('entrada.txt') as file:
        lines = file.readlines()

    text = ''
    for line in lines:
        line = line.replace('\n', '')
        # print(repr(line))
        text = text + line

    turing_machine, entrada = text.split('000')[1:-1]

    transitions_list = turing_machine.split('00')
    # print(transitions_list)
    
    max_state = 0
    max_input = 0
    
    transitions = {}
    for t in transitions_list:
        current_state, input_symbol, next_state, new_symbol, direction = t.split('0')
        current_state = len(current_state)
        input_symbol = len(input_symbol)
        next_state = len(next_state)
        print(next_state)
        new_symbol = len(new_symbol)
        direction = len(direction)
        
        max_state = max(max_state, next_state, current_state)
        print(max_state)
        max_input = max(max_input, input_symbol)
        
        transitions[(current_state, input_symbol)] = (next_state, new_symbol, direction)

    entrada = entrada.split('0')
    tape = {}

    for i in range(0, len(entrada)):
        tape[i] = len(entrada[i])

    return transitions, tape, max_state, max_input





def main():
    transitions, tape, max_state, max_input = decode_UTM_text()
    
    turingMachine = MT(alphabet_symbols= range(1, max_input) , blank= max_input, input_symbols = range(1, max_input), states= range(1, max_state), initial_state=1, transitions=transitions, tape=tape)

    while not turingMachine.halted:
        turingMachine.print()
        turingMachine.step()
    print("halted")


if __name__ == '__main__':
    main()

from turingMachine import MT


# Decodificador:
# turing machine
def decode_UTM_text():
    with open('entrada.txt') as file:
        lines = file.readlines()

    text = ''
    for line in lines:
        line = line.replace('\n', '')
        print(repr(line))
        text = text + line

    turing_machine, entrada = text.split('000')[1:-1]

    transitions_list = turing_machine.split('00')
    print(transitions_list)

    transitions = {}
    for t in transitions_list:
        current_state, input_symbol, next_state, new_symbol, direction = t.split('0')
        transitions[(current_state, input_symbol)] = (next_state, new_symbol, direction)

    entrada = entrada.split('0')
    tape = {}

    for i in range(0, len(entrada)):
        tape[i] = entrada[i]

    return transitions, tape





def main():
    transitions, tape = decode_UTM_text()
    turingMachine = MT(alphabet_symbols=['1','11','111'], blank='111',input_symbols=['1','11','111'], states=['1','11','111','1111'], initial_state='1', transitions=transitions, tape=tape)

    while not turingMachine.halted:
        turingMachine.print_state()
        turingMachine.step()
    print("halted")


if __name__ == '__main__':
    main()


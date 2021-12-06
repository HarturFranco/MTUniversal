"""
Feito por:
- Arthur Silveira Franco
- Iorrana Maria do Nascimento
- Joao Paulo Paiva Lima

Script principal, contem a funcao de decodificacao da maquina de turing
e executa a maquina no metodo principal.
"""
import sys
from turingMachine import MTU


# Decodificador:
# turing machine
def decode_UTM_text(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    text = ''
    for line in lines:
        line = line.replace('\n', '')
        text = text + line

    turing_machine, entrada = text.split('000')[1:-1]

    transitions_list = turing_machine.split('00')
    num_state = 0
    num_input = 0
    
    transitions = {}
    for t in transitions_list:
        current_state, input_symbol, next_state, new_symbol, direction = t.split('0')
        current_state = len(current_state)
        input_symbol = len(input_symbol)
        next_state = len(next_state)
        
        new_symbol = len(new_symbol)
        direction = len(direction)
        
        num_state = max(num_state, next_state, current_state)
        num_input = max(num_input, input_symbol)
        
        transitions[(current_state, input_symbol)] = (next_state, new_symbol, direction)

    entrada = entrada.split('0')
    tape = {}
    for i in range(0, len(entrada)):
        tape[i] = len(entrada[i]) if len(entrada[i]) != 0 else num_input # Entrada vazia = maxInput (blank) para as entradas = 3

    return transitions, tape, num_state, num_input


def main():
    # decodifica maquina de turing e entrada
    transitions, tape, num_state, num_input = decode_UTM_text(sys.argv[1])
    # instancia maquina de turing decodificada
    turingMachine = MTU(alphabet_symbols= range(1, num_input) , blank= num_input,
                    input_symbols = range(1, num_input), states= range(1, num_state+1),
                    initial_state=1, transitions=transitions, tape=tape)

    # execucao da maquina
    try:
        while not turingMachine.halted:
            turingMachine.print()
            turingMachine.step()

        print("Parou!")
    except RuntimeError as e:
        print(e.args[0])


if __name__ == '__main__':
    main()

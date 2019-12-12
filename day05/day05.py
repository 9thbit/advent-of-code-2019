

def read_input(filename):
    with open(filename, "rt") as input_file:
        return list(map(int, input_file.readline().split(',')))


def run_program(program):
    ADD_OPCODE, MULTIPLY_OPCODE, END_OPCODE = 1, 2, 99
    memory = program[:]
    codes = iter(memory)
    while codes:
        opcode = next(codes)
        if opcode == END_OPCODE:
            break

        argument1_position = next(codes)
        argument2_position = next(codes)
        output_position = next(codes)

        argument1 = memory[argument1_position]
        argument2 = memory[argument2_position]

        if opcode == ADD_OPCODE:
            output_value = argument1 + argument2
        elif opcode == MULTIPLY_OPCODE:
            output_value = argument1 * argument2
        else:
            raise NotImplementedError(f'{opcode=}')

        memory[output_position] = output_value

    return memory


def main():
    filename = "input.txt"
    input_program = read_input(filename)


if __name__ == "__main__":
    main()

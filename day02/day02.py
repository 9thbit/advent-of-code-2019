from itertools import product


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

    input_program[1:3] = [12, 2]
    memory = run_program(input_program)
    print(f'Part 1: {memory[0]}')

    for noun, verb in product(list(range(1, 100)), repeat=2):
        input_program[1:3] = [noun, verb]
        memory = run_program(input_program)
        if memory[0] == 19690720:
            print(f'Part 2: {100 * noun + verb}')
            break


if __name__ == "__main__":
    main()

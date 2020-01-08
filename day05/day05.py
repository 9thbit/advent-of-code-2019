from enum import IntEnum


class Opcodes(IntEnum):
    ADD_OPCODE = 1
    MULTIPLY_OPCODE = 2
    INPUT_OPCODE = 3
    OUTPUT_OPCODE = 4
    END_OPCODE = 99


class ArgumentMode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


def read_input(filename):
    with open(filename, "rt") as input_file:
        return list(map(int, input_file.readline().split(',')))


def disect_instruction(instruction):
    opcode = instruction % 100
    paramter1_mode = (instruction // 100) % 10
    paramter2_mode = (instruction // 1000) % 10
    paramter3_mode = (instruction // 10000) % 10
    return opcode, paramter1_mode, paramter2_mode, paramter3_mode


def run_program(program, input_stream, output_stream):

    memory = program[:]
    instructions = iter(memory)

    def get_argument(argument_mode):
        arg_value = next(instructions)
        if argument_mode == ArgumentMode.POSITION:
            return memory[arg_value]
        elif argument_mode == ArgumentMode.IMMEDIATE:
            return arg_value
        else:
            raise NotImplementedError(f'{argument_mode=}')

    while instructions:
        instruction = next(instructions)
        opcode, paramter1_mode, paramter2_mode, paramter3_mode = disect_instruction(instruction)
        if opcode == Opcodes.END_OPCODE:
            break

        if opcode == Opcodes.ADD_OPCODE:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            output_position = next(instructions)
            memory[output_position] = argument1 + argument2

        elif opcode == Opcodes.MULTIPLY_OPCODE:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            output_position = next(instructions)
            memory[output_position] = argument1 * argument2

        elif opcode == Opcodes.INPUT_OPCODE:
            output_position = next(instructions)
            output_value = next(input_stream)
            memory[output_position] = output_value

        elif opcode == Opcodes.OUTPUT_OPCODE:
            value_position = next(instructions)
            output_stream.append(memory[value_position])

        else:
            raise NotImplementedError(f'{opcode=}')

    return memory


def main():
    filename = "input.txt"
    input_program = read_input(filename)

    input_stream = [1]
    output_stream = []
    memory = run_program(input_program, iter(input_stream), output_stream)
    print(f'Part 1: {output_stream[-1]}')


if __name__ == "__main__":
    main()

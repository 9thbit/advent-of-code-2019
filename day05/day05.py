from enum import IntEnum


class Opcodes(IntEnum):
    ADD_OPCODE = 1
    MULTIPLY_OPCODE = 2
    INPUT_OPCODE = 3
    OUTPUT_OPCODE = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
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


class Computer:

    def __init__(self, program):
        self.memory = program[:]
        self.instruction_pointer = 0

    def next(self):
        assert self.has_next()
        value = self.memory[self.instruction_pointer]
        self.instruction_pointer += 1
        return value

    def has_next(self):
        return 0 <= self.instruction_pointer < len(self.memory)

    def jump(self, target_instruction_pointer):
        assert 0 <= target_instruction_pointer < len(self.memory)
        self.instruction_pointer = target_instruction_pointer


def run_program(program, input_stream, output_stream):

    computer = Computer(program)

    def get_argument(argument_mode):
        arg_value = computer.next()
        if argument_mode == ArgumentMode.POSITION:
            return computer.memory[arg_value]
        elif argument_mode == ArgumentMode.IMMEDIATE:
            return arg_value
        else:
            raise NotImplementedError(f'{argument_mode=}')

    while computer.has_next():
        instruction = computer.next()
        opcode, paramter1_mode, paramter2_mode, paramter3_mode = disect_instruction(instruction)
        if opcode == Opcodes.END_OPCODE:
            break

        if opcode == Opcodes.ADD_OPCODE:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            output_position = computer.next()
            computer.memory[output_position] = argument1 + argument2

        elif opcode == Opcodes.MULTIPLY_OPCODE:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            output_position = computer.next()
            computer.memory[output_position] = argument1 * argument2

        elif opcode == Opcodes.INPUT_OPCODE:
            output_position = computer.next()
            output_value = next(input_stream)
            computer.memory[output_position] = output_value

        elif opcode == Opcodes.OUTPUT_OPCODE:
            value = get_argument(paramter1_mode)
            output_stream.append(value)

        elif opcode == Opcodes.JUMP_IF_TRUE:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            if argument1 != 0:
                computer.jump(argument2)

        elif opcode == Opcodes.JUMP_IF_FALSE:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            if argument1 == 0:
                computer.jump(argument2)

        elif opcode == Opcodes.LESS_THAN:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            output_position = computer.next()
            computer.memory[output_position] = int(argument1 < argument2)

        elif opcode == Opcodes.EQUALS:
            argument1 = get_argument(paramter1_mode)
            argument2 = get_argument(paramter2_mode)
            output_position = computer.next()
            computer.memory[output_position] = int(argument1 == argument2)

        else:
            raise NotImplementedError(f'{opcode=}')

    return computer.memory


def main():
    filename = "input.txt"
    input_program = read_input(filename)

    input_stream = [1]
    output_stream = []
    run_program(input_program, iter(input_stream), output_stream)
    print(f'Part 1: {output_stream[-1]}')

    input_stream = [5]
    output_stream = []
    run_program(input_program, iter(input_stream), output_stream)
    print(f'Part 2: {output_stream[-1]}')


if __name__ == "__main__":
    main()

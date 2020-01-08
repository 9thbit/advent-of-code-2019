import pytest

from day05 import Opcodes, run_program


@pytest.mark.parametrize("program, expected_output", [
    ([1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99]),  # 3 * 33, store the result in position 4
    ([1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]),  # 100 + -1, store the result in position 4
])
def test_sample_programs(program, expected_output):
    assert run_program(program, None, None) == expected_output


@pytest.mark.parametrize("program, input_data, expected_output", [
    ([Opcodes.INPUT_OPCODE, 2, 0], [99], [Opcodes.INPUT_OPCODE, 2, 99]),
    ([Opcodes.INPUT_OPCODE, 1, 99], [5], [Opcodes.INPUT_OPCODE, 5, 99]),
])
def test_input_programs(program, input_data, expected_output):
    assert run_program(program, iter(input_data), None) == expected_output


@pytest.mark.parametrize("program, expected_output", [
    ([Opcodes.OUTPUT_OPCODE, 0, 99], [Opcodes.OUTPUT_OPCODE]),
    ([Opcodes.OUTPUT_OPCODE, 1, 99], [1]),
    ([Opcodes.OUTPUT_OPCODE, 2, 99], [99]),
])
def test_output_programs(program, expected_output):
    output_list = []
    assert run_program(program, None, output_list) == program
    assert output_list == expected_output


@pytest.mark.parametrize("program, input_data, expected_output", [
    # position mode: output 1 if input is equal to 8, otherwise 0
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [7], [0]),
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8], [1]),
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [9], [0]),

    # position mode: output 1 if input is less than 8, otherwise 0
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [6], [1]),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [7], [1]),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [8], [0]),

    # immediate mode: output 1 if input is equal to 8, otherwise 0
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [7], [0]),
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [8], [1]),
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [9], [0]),

    # immediate mode: output 1 if input is less than 8, otherwise 0
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [6], [1]),
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [7], [1]),
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [8], [0]),
])
def test_input_output_programs(program, input_data, expected_output):
    output_stream = []
    run_program(program, iter(input_data), output_stream)
    assert output_stream == expected_output


@pytest.mark.parametrize("program, input_data, expected_output", [
    # take an input, then output 0 if the input was zero or 1 if the input was non-zero

    # position mode
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [0], [0]),
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [1], [1]),
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [2], [1]),

    # immediate mode
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [0], [0]),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [1], [1]),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [2], [1]),
])
def test_jump_programs(program, input_data, expected_output):
    output_stream = []
    run_program(program, iter(input_data), output_stream)
    assert output_stream == expected_output


@pytest.mark.parametrize("input_data, expected_output", [
    ([5], [999]),
    ([6], [999]),
    ([7], [999]),
    ([8], [1000]),
    ([9], [1001]),
    ([10], [1001]),
    ([11], [1001]),
])
def test_large_example(input_data, expected_output):
    # output 999, 1000, 1001 if the input value is respectively below, equal, or greater than 8
    program = [
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99,
    ]
    output_stream = []
    run_program(program, iter(input_data), output_stream)
    assert output_stream == expected_output

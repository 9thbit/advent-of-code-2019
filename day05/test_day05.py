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

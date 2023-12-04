import pytest
import utils

@pytest.mark.parametrize(
    "input_file, expected_output_file",
    [
        ("exercise1_assembler_output.mx", "exercise1_expected_output.mx")
    ]
)
def test_assembled_output_matches_expected(input_file, expected_output_file):

    with open(expected_output_file, "r") as file:
        expected_output_file = file.read()
        expected_output_file = "\n".join(filter(None, expected_output_file.splitlines()))

    assert utils.generate_mx_file_from_as(input_file) == expected_output_file

@pytest.mark.parametrize(
    "input_file, expected_output_file",
    [
        ("exercise1_assembler_output.mx", "exercise1_expected_vm_output.txt")
    ]
)
def test_virtual_machine_output_matches_expected(input_file, expected_output_file):
    with open(expected_output_file, "r") as file:
        expected_output = file.read()
        expected_output = "\n".join(filter(None, expected_output.splitlines()))
    assert utils.generate_vm_output_from_mx(input_file) == expected_output

@pytest.mark.parametrize(
    "input_file",
    [
        "exercise1_test_out_of_memory.mx"
    ]
)
def test_out_of_memory_error(input_file):
    expected_error_message = "Program is too long for memory"
    assert expected_error_message in utils.generate_out_of_memory_error(input_file)

@pytest.mark.parametrize(
    "input_file, error_msg",
    [
        ("exercise1_test_instruction_not_found.mx", "Unknown op 000016")
    ]
)
def test_instruction_not_found_error(input_file, error_msg):
    assert error_msg in utils.generate_instruction_not_found_error(input_file)

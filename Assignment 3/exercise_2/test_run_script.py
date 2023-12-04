import pytest
import subprocess

def generate_disassembler_output(input_file, output_file):
    subprocess.run(["python", "disassembler.py", input_file, output_file])

    with open(output_file, "r") as file:
        generated_file = file.read()
        generated_file = "\n".join(filter(None, generated_file.splitlines()))

    return generated_file

@pytest.mark.parametrize(
    "input_file, output_file, expected_output",
    [
        ("example_input.mx", "example_output.as", "expected_output.as")
    ]
)
def test_disassembler(input_file, output_file, expected_output):

    with open(expected_output, "r") as file:
        expected_output_file = file.read()
        expected_output_file = "\n".join(filter(None, expected_output_file.splitlines()))

    assert generate_disassembler_output(input_file, output_file) == expected_output_file

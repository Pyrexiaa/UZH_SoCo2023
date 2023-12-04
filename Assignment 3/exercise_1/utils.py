import subprocess

def generate_mx_file_from_as(input_file):
    subprocess.run(["python", "../debugger/assembler.py", "exercise1.as", input_file])
    generated_file = "exercise1_assembler_output.mx"

    with open(generated_file, "r") as file:
        generated_file = file.read()
        generated_file = "\n".join(filter(None, generated_file.splitlines()))

    return generated_file

def generate_vm_output_from_mx(input_file):
    result = subprocess.run(
        ["python", "../debugger/vm_base.py", input_file],
        capture_output=True,
        text=True 
    )

    result_output = "\n".join(filter(None, result.stdout.splitlines()))
    return result_output

def generate_out_of_memory_error(input_file):
    result = subprocess.run(
        ["python", "../debugger/vm_base.py", input_file],
        capture_output=True,
        text=True 
    )
    return result.stderr

def generate_instruction_not_found_error(input_file):
    result = subprocess.run(
        ["python", "../debugger/vm_base.py", input_file],
        capture_output=True,
        text=True 
    )
    return result.stderr

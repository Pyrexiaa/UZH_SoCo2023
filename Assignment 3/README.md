# Virtual Machines and Debuggers

## Virtual Machines

A virtual machine represents a simulated computer, complete with a processor, registers, and memory. Instructions, usually represented as assembly code, dictate the operations the processor performs. These instructions may involve registers, memory, or both. Processors typically execute instructions sequentially, but conditional statements allow for jumps based on certain conditions.

## Debuggers

Debuggers play a crucial role in testing and simulating interactive programs. By simulating input and capturing output, developers can efficiently test their programs. Debuggers often use breakpoints, where actual instructions are temporarily replaced with special ones for inspection. Utilizing lookup tables for function or method dispatch enhances program extensibility.

# Table of Contents

1. Exercise 1: Unit Testing

- 1.1 File Structure
- 1.2 Unit Testing
  - 1.2.1 Assembler Testing
  - 1.2.2 Virtual Machine Testing
  - 1.2.3 Error Testing
- 1.3 Test Coverage

2. Exercise 2: Disassembler

- 2.1 File Structure
- 2.2 Disassembler Implementation
- 2.3 Testing

3. Exercise 3: New Features and Problems - Assembler

- 3.1 File Structure
- 3.2 New Features
  - 3.2.1 Increment and Decrement
  - 3.2.2 Swap Values
  - 3.2.3 Reverse Array in Place

4. Exercise 4: New Features - Debugger

- 4.1 File Structure
- 4.2 New Features
  - 4.2.1 Show Memory Range
  - 4.2.2 Breakpoint Addresses
  - 4.2.3 Command Completion
  - 4.2.4 Watchpoints

# Exercise 1: Unit Testing

This project focuses on unit testing the Assembler and Virtual Machine implemented in Chapters 25 and 26, respectively. The testing is done using the pytest framework.

## File Structure

The project structure is organized as follows:

- `exercise_1/`: Main exercise directory.
  - `exercise1.as`: Sample assembly program for testing the Assembler.
  - `exercise1_assembler_output.mx`: Assembly code output for the sample assembly program.
  - `exercise1_expected_output.mx`: Expected output for the Virtual Machine when executing the sample program.
  - `exercise1_expected_vm_output.txt`: Expected output for the Virtual Machine.
  - `exercise1_test_instruction_not_found.mx`: Assembly code output that contains operation code that is not included in the program.
  - `exercise1_test_out_of_memory.as`: Test case for an out-of-memory scenario.
  - `exercise1_test_out_of_memory.mx`: Expected output for the out-of-memory test.
  - `test_run_script.py`: Script for running the tests.
  - `trace/`: Directory containing trace files generated during testing.
  - `utils.py`: Utility functions for testing.

## Unit Testing

### Assembler Testing

1. **Write Assembly Programs:**

   - Create assembly programs in `.as` files, e.g., `exercise1.as`.

2. **Manual Calculation:**

   - Manually calculate expected output VM instructions for each assembly program.
   - The expected output `.mx` file is stored as `exercise1_expected_output.mx`.

3. **Assembler Execution:**

   - Run assembly programs through the Assembler to produce `.mx` files.
   - The output is stored as `exercise1_assembler_output.mx`.

4. **Comparison:**
   - Compare the output of the Assembler to the manually calculated VM instructions.
   - `exercise1_assembler_output.mx` is compared with `exercise1_expected_output.mx`.

### Virtual Machine Testing

1. **Assumption:**

   - Assume the correctness of the Assembler.

2. **VM Execution:**

   - Run the `.mx` files produced by the Assembler through the Virtual Machine.

3. **Output Comparison:**
   - Compare the output of the Virtual Machine with the expected output, stored as `exercise1_expected_vm_output.txt`.
   - The comparison result is printed in the terminal.

### Error Testing

1. **Out-of-memory Error:**

   - `exercise1_test_out_of_memory.as` contains assembly code that requests memory beyond the VM's capacity.
   - `exercise1_test_out_of_memory.mx` contains the assembly programs from `exercise1_test_out_of_memory.as`
   - The output for the out-of-memory test is asserted to have out of memory error message.

2. **Instruction-not-found Error:**
   - `exercise1_test_instruction_not_found.mx` contains assembled code with an unknown instruction (operations).
   - The output for the instruction not found error is asserted to have unknown operation message.

### Utilities & Run Script

1. **Utilities**

   - This script contains 4 functions to generate outputs for:
     - `.as` to `.mx` files.
     - `vm` output from `.mx` files.
     - error message from `out of memory` files.
     - error message from `instruction not found` files.

2. **Run Script**
   - This script contains 4 test functions and assert output from utilities to be the same with expected input.
   - Running `pytest --cov` will run this script.

## Test Coverage

The test coverage for this project is measured using `pytest --cov`. To reproduce the coverage report, follow these steps:

1. **Measure Test Coverage:**
   - Use pytest and coverage to measure test coverage.
     - Install pytest-cov:
       ```
       pip install pytest-cov
       ```
     - Run pytest with coverage:
       ```
       pytest --cov
       ```
   - The test coverage percentage will be displayed in the terminal.

# Exercise 2: Disassembler

This project involves the implementation of a disassembler, a tool that converts Virtual Machine (VM) instructions from a `.mx` file to assembly code in a `.as` file. The disassembler is designed to be run from the command line.

## File Structure

The project structure is organized as follows:

- `exercise_2/`: Main project folder.
  - `disassemble.py`: Python script for the disassembler implementation.
  - `input_file.mx`: Sample input VM instructions for testing.
  - `output_file.as`: Sample output assembly code after disassembly.
  - `expected_output.as`: Expected assembly code for comparison in tests.
  - `test_run_script.py`: Python test script for the disassembler.

## Disassembler Implementation

### Running the Disassembler

To run the disassembler, execute the following command from the command line:

```
python disassemble.py input_file.mx output_file.as
```

To generate test coverage for this exercise, please run `pytest --cov` in this directory.

# Exercise 3: New Features and Problems - Assembler

In this exercise, new features are added to the assembly language, and corresponding problems are presented. The instructions include incrementing, decrementing, swapping values, and reversing an array in place.

## File Structure

The project structure is organized as follows:

- `exercise_3/`: Main project directory.
  - `example_3_1.as`: Example assembly program for incrementing and decrementing.
  - `example_3_2.as`: Example assembly program for swapping values.
  - `example_3_3.as`: Example assembly program for reversing an array.
  - `output_3_1.mx`: Output machine code for example 3.1.
  - `output_3_2.mx`: Output machine code for example 3.2.
  - `output_3_3.mx`: Output machine code for example 3.3.

## New Features

### 3.1 Increment and Decrement

#### Implementation

Two new instructions, `inc` and `dec`, have been added to the assembly language. `inc` adds one to the value of a register, and `dec` subtracts one from the value of a register.

#### Usage

To use these instructions, modify the `architecture.py` and `assembler.py` files in the `vm/` directory. An example program (`example_3_1.as`) demonstrates the usage:

```
python ../vm/assembler.py example_3_1.as output_3_1.mx
```

To see the output of the new instructions, you may run the command as shown below.

```
python ../vm/vm.py output_3_1.mx
```

### 3.2 Swap Values

### Implementation

A new instruction, `swp R1 R2`, has been added to the assembly language. This instruction swaps the values in registers R1 and R2 without affecting other registers.

### Usage

To use this instruction, modify the architecture.py and assembler.py files in the vm/ directory. An example program (example_3_2.as) demonstrates the usage:

```
python ../vm/assembler.py example_3_2.as output_3_2.mx
```

To see the output of the new instructions, you may run the command as shown below.

```
python ../vm/vm.py output_3_2.mx
```

### 3.3 Reverse Array in Place

### Implementation

A program has been implemented to reverse an array in place. The program takes the base address of an array, the length of the array, and the array values as input.

### Usage

To use this program, modify the architecture.py and assembler.py files in the vm/ directory. An example program (example_3_3.as) demonstrates the usage:

Comments are added in example_3_3.as files to explain further on the code works as well as in reversing the array

```
python ../vm/assembler.py example_3_3.as output_3_3.mx
```

To see the output of the new instructions, you may run the command as shown below.

```
python ../vm/vm.py output_3_3.mx
```

# Exercise 4: New Features - Debugger

In this exercise, several new features are added to the debugger to enhance its functionality. The features include showing memory ranges, setting/clearing breakpoints, command completion, and watchpoints.

## File Structure

The project structure is organized as follows:

- `debugger/`: Main debugger directory.
  - `architecture.py`: File defining the architecture of the virtual machine.
  - `assembler.py`: File containing the implementation of the assembler.
  - `count_up.as`: Example assembly program for testing.
  - `count_up.mx`: Corresponding machine code for the example program.
  - `vm_base.py`: Base file for the virtual machine.
  - `vm_break.py`: File for handling breakpoints in the virtual machine.
  - `vm_extend.py`: File containing extended functionality for the virtual machine.
  - `vm_step.py`: File for stepping through the virtual machine instructions.
  - `watchpoint_example.as`: Example assembly program demonstrating watchpoints.
  - `watchpoint_example.mx`: Corresponding machine code for the watchpoint example.

## New Features

### 4.1 Show Memory Range

#### Implementation

Modify the `vm_extend.py` file in debugger directory to enable the debugger to show the value at a single address or all memory between two addresses using the "memory" command.

#### Testing Instructions

Interactively test this feature with the following commands:

```
python vm_extend.py count_up.mx
```

1. You can enter the address directly and its value will be shown.

- 000000 [dimqrs]> 4
- Address provided: 4
- Value of that address: 020006

2. You can enter the range of address directly and the value in between will be shown.

- 000001 [dimqrs]> 1 3
- Address provided: 1 3
- Value between this range of address: 030102 00000d

3. You can enter the command (amended due to the requirements in the later question) and the current value will be shown.

- 000000 [dimqrs]> show
- Function Called: \_do_show_memory_range
- Address provided: 0
- Value of that address: 000002

### 4.2 Breakpoint Addresses

### Implementation

Modify the `vm_break.py` file in debugger directory to allow users to set or clear breakpoints at a single address using the "break" or "clear" command.

### Testing Instructions

Interactively test this feature with the following commands:

```
python vm_break.py count_up.mx
```

1. You can enter the first string as the command with the second integer as the address to `add` the breakpoint

- 000000 [bcdimqrs]> b 4
- Function Called: \_do_add_breakpoint
- Added breakpoint at 000004

- 000000 [bcdimqrs]> add_break 4
- Function Called: \_do_add_breakpoint
- Added breakpoint at 000004

2. You can enter the first string as the command with the second integer as the address to `clear` the breakpoint

- 000001 [bcdimqrs]> c 4
- Function Called: \_do_clear_breakpoint
- Cleared breakpoint at 000004

- 000001 [bcdimqrs]> clear 4
- Function Called: \_do_clear_breakpoint
- Cleared breakpoint at 000004

### 4.3 Command Completion

### Implementation

Modify the `vm_extend.py` and `vm_break.py` files in debugger directory to recognize commands based on any number of distinct leading characters. For example, "m," "me," "mem," and so on should trigger the "do_memory" method.

### Testing Instructions

Interactively test this feature by providing partial commands:

```
python vm_break.py count_up.mx
```

As shown above, we can provide partial commands in adding and clearing breakpoints with following the key value stated in the dictionary.

We will first search if there is any function's name starting with the input characters, if not, we will select the function with the characters in it, else we will return `Unknown Command`.

### 4.4 Watchpoints

### Implementation

Modify the `vm_break.py` file in the debugger directory and VM to support watchpoints, allowing the debugger to halt the VM when the value at a specified address changes.

### Testing Instructions

Interactively test this feature with the following commands:

```
python vm_break.py watchpoint_example.mx
```

The user can add a watchpoint at the particular address by running command as below:

- 000000 [bcdimqrs]> watch 100
- Function Called: \_do_add_watchpoint
- Added watchpoint at 100

In the `.mx` file provided, changing in the address value has occurred while reversing the array at the 100th ip address.
Therefore, the program is halted once detected there are changes occurred at that particular ip address.

- 000001 [bcdimqrs]> r
- Function Called: \_do_run
- 000005
- Changes detected at IP 000005

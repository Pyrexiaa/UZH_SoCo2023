from enum import Enum


OPS = {
    "hlt": {"code": 1, "fmt": "--"},  # Halt program
    "ldc": {"code": 2, "fmt": "rv"},  # Load immediate
    "ldr": {"code": 3, "fmt": "rr"},  # Load register
    "cpy": {"code": 4, "fmt": "rr"},  # Copy register
    "str": {"code": 5, "fmt": "rr"},  # Store register
    "add": {"code": 6, "fmt": "rr"},  # Add
    "sub": {"code": 7, "fmt": "rr"},  # Subtract
    "inc": {"code": 8, "fmt": "r-"},  # Increase by 1
    "dec": {"code": 9, "fmt": "r-"},  # Decrease by 1
    "swp": {"code": 10, "fmt": "rr"},  # Swap register
    "beq": {"code": 11, "fmt": "rv"},  # Branch if equal
    "bne": {"code": 12, "fmt": "rv"},  # Branch if not equal
    "prr": {"code": 13, "fmt": "r-"}, # Print register
    "prm": {"code": 14, "fmt": "r-"}, # Print memory
    "brk": {"code": 15, "fmt": "--"}, # Breakpoint
    "wth": {"code": 16, "fmt": "--"}, # Watchpoint
}

OP_MASK = 0xFF  # select a single byte
OP_SHIFT = 8  # shift up by one byte
OP_WIDTH = 6  # op width in characters when printing

NUM_REG = 5  # number of registers
RAM_LEN = 256  # number of words in RAM

# [state]
class VMState(Enum):
    """Virtual machine states."""
    FINISHED = 0
    STEPPING = 1
    RUNNING = 2
# [/state]

import sys

# OPS = {
#     "hlt": {"code": 1, "fmt": "--"},  # Halt program
#     "ldc": {"code": 2, "fmt": "rv"},  # Load immediate
#     "ldr": {"code": 3, "fmt": "rr"},  # Load register
#     "cpy": {"code": 4, "fmt": "rr"},  # Copy register
#     "str": {"code": 5, "fmt": "rr"},  # Store register
#     "add": {"code": 6, "fmt": "rr"},  # Add
#     "sub": {"code": 7, "fmt": "rr"},  # Subtract
#     "beq": {"code": 8, "fmt": "rv"},  # Branch if equal
#     "bne": {"code": 9, "fmt": "rv"},  # Branch if not equal
#     "prr": {"code": 10, "fmt": "r-"},  # Print register
#     "prm": {"code": 11, "fmt": "r-"},  # Print memory
#     "brk": {"code": 15, "fmt": "--"},  # Breakpoint
# }

OPS = {
        1: {"code": "hlt", "fmt": "--"},
        2: {"code": "ldc", "fmt": "rv"},
        3: {"code": "ldr", "fmt": "rr"},
        4: {"code": "cpy", "fmt": "rr"},
        5: {"code": "str", "fmt": "rr"},
        6: {"code": "add", "fmt": "rr"},
        7: {"code": "sub", "fmt": "rr"},
        8: {"code": "beq", "fmt": "rv"},
        9: {"code": "bne", "fmt": "rv"},
        10: {"code": "prr", "fmt": "r-"},
        11: {"code": "prm", "fmt": "r-"},
        15: {"code": "brk", "fmt": "--"},
}

NUM_REG = 4  # number of registers
RAM_LEN = 256  # number of words in RAM

class Disassembler:
    def __init__(self, labels):
        self.labels = labels

    def disassemble(self, instructions):
        lines = self.clean_lines(instructions)
        result = []
        for line in lines:
            args, op = self._disassemble(line)
            line = self._format_instruction(args, op)
            result.append(line)
        # If there's a label
        if len(self.labels) != 0:
            for label, location in self.labels.items():
                result.insert(location, f"{label}:")
        return result

    def _disassemble(self, instruction):
        # Value, Register, Operation
        args = [instruction[:-4], instruction[-4:-2]]
        op = instruction[-2:]
        op = int(op, 16)
        args = [int(section, 16) for section in args]
        return args, op

    def _format_instruction(self, args, op):
        code = OPS[op]["code"]
        fmt = OPS[op]["fmt"]
        reg_or_value = args[0]
        reg = args[1]
        assert reg < NUM_REG

        if fmt == "--":
            return f"{code}"
        
        elif fmt == "rv":
            # If there's a branch
            if code == "bne" or code == "beq":
                index = reg_or_value
                label = self._get_label(index)
                return f"{code} R{reg} @{label}"
            
            reg_or_value = format(reg_or_value, '02x')
            if reg_or_value[0] == '0':
                reg_or_value = reg_or_value[1]
            return f"{code} R{reg} {reg_or_value}"
        
        elif fmt == "rr":
            assert reg_or_value < NUM_REG
            return f"{code} R{reg} R{reg_or_value}"
        
        elif fmt == "r-":
            return f"{code} R{reg}"

    def _get_label(self, loc):
        for label, location in self.labels.items():
            if location == loc:
                return label
        return None
    
    def clean_lines(self, lines):
        lines = [ln.strip() for ln in lines]
        lines = [ln for ln in lines if len(ln) > 0]
        return lines

def main(disassembler_cls):
    assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} input|- output|-"
    reader = open(sys.argv[1], "r") if (sys.argv[1] != "-") else sys.stdin
    writer = open(sys.argv[2], "w") if (sys.argv[2] != "-") else sys.stdout
    lines = reader.readlines()
    disassembler = disassembler_cls({"loop":2})
    program = disassembler.disassemble(lines)
    for instruction in program:
        print(instruction, file=writer)

if __name__ == "__main__":
    main(Disassembler)
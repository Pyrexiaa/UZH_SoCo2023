import sys
from architecture import NUM_REG, OPS, OP_MASK, OP_SHIFT, RAM_LEN

COLUMNS = 4
DIGITS = 8


# [init]
class VirtualMachine:
    def __init__(self):
        self.initialize([])
        self.prompt = ">>"

    def initialize(self, program):
        assert len(program) <= RAM_LEN, "Program too long"
        self.ram = [
            program[i] if (i < len(program)) else 0
            for i in range(RAM_LEN)
        ]
        self.ip = 0
        self.reg = [0] * NUM_REG
# [/init]

    # [fetch]
    def fetch(self):
        instruction = self.ram[self.ip]
        self.ip += 1
        op = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg0 = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg1 = instruction & OP_MASK
        return [op, arg0, arg1]
    # [/fetch]

    def show(self, writer = sys.stdout):
        print(f"IP{' ' * 6}= {self.ip:06x}", file=writer)
        # Show registers
        for (i, r) in enumerate(self.reg):
            print(f"R{i:06x} = {r:06x}", file=writer)

        # How much memory to show
        top = max(i for (i, m) in enumerate(self.ram) if m != 0)

        # Show memory
        base = 0
        while base <= top:
            output = f"{base:06x}: "
            for i in range(COLUMNS):
                output += f"  {self.ram[base + i]:06x}"
            print(output, file=writer)
            base += COLUMNS

    # [run]
    def run(self):
        running = True
        while running:
            op, arg0, arg1 = self.fetch()
            if op == OPS["hlt"]["code"]:
                running = False
            elif op == OPS["ldc"]["code"]:
                self.assert_is_register(arg0)
                self.reg[arg0] = arg1
            elif op == OPS["ldr"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_register(arg1)
                self.reg[arg0] = self.ram[self.reg[arg1]]
            elif op == OPS["cpy"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_register(arg1)
                self.reg[arg0] = self.reg[arg1]
            # [skip]
            # [store]
            elif op == OPS["str"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_register(arg1)
                self.ram[self.reg[arg1]] = self.reg[arg0]
            # [/store]
            # [/add]
            elif op == OPS["add"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_register(arg1)
                self.reg[arg0] += self.reg[arg1]
            # [/minus]
            elif op == OPS["sub"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_register(arg1)
                self.reg[arg0] -= self.reg[arg1]
            # [/swap]
            elif op == OPS["swp"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_register(arg1)
                temp = self.reg[arg0]
                self.reg[arg0] = self.reg[arg1]
                self.reg[arg1] = temp
                del temp
            # [/increase]
            elif op == OPS["inc"]["code"]:
                self.assert_is_register(arg0)
                self.reg[arg0] += 1
            # [/decrease]
            elif op == OPS["dec"]["code"]:
                self.assert_is_register(arg0)
                self.reg[arg0] -= 1
            # [beq]
            elif op == OPS["beq"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_address(arg1)
                if self.reg[arg0] == 0:
                    self.ip = arg1
            # [/beq]
            elif op == OPS["bne"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_address(arg1)
                if self.reg[arg0] != 0:
                    self.ip = arg1
            elif op == OPS["prr"]["code"]:
                self.assert_is_register(arg0)
                print(self.prompt, self.reg[arg0])
            elif op == OPS["prm"]["code"]:
                self.assert_is_register(arg0)
                self.assert_is_address(self.reg[arg0])
                print(self.prompt, self.ram[self.reg[arg0]])
            # [/skip]
            else:
                assert False, f"Unknown op {op:06x}"

    def assert_is_register(self, reg):
        assert 0 <= reg < len(self.reg), f"Invalid register {reg:06x}"

    def assert_is_address(self, addr):
        assert 0 <= addr < len(self.ram), f"Invalid register {addr:06x}"

    # [/run]


def main(vm_cls):
    assert len(sys.argv) >= 2, f"Usage: {sys.argv[0]} input|- output|-"
    reader = open(sys.argv[1], "r") if (sys.argv[1] != "-") else sys.stdin
    if len(sys.argv) > 2:
        assert len(sys.argv) == 3, "Maximum only 2 arguments!"
        writer = open(sys.argv[2], "w") if (sys.argv[2] != "-") else sys.stdout

    lines = [ln.strip() for ln in reader.readlines()]
    program = [int(ln, 16) for ln in lines if ln]
    vm = vm_cls()
    vm.initialize(program)
    vm.run()
    if len(sys.argv) == 3:
        vm.show(writer)
    vm.show()


if __name__ == "__main__":
    main(VirtualMachine)

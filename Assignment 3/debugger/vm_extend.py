import sys
import difflib
from architecture import VMState, RAM_LEN
from vm_step import VirtualMachineStep


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.handlers = {
            "d": self._do_disassemble,
            "dis": self._do_disassemble,
            "i": self._do_ip,
            "ip": self._do_ip,
            "m": self._do_memory,
            "memory": self._do_memory,
            "q": self._do_quit,
            "quit": self._do_quit,
            "r": self._do_run,
            "run": self._do_run,
            "s": self._do_step,
            "step": self._do_step,
        }
        self.first_input = None
        self.second_input = None
        self.functions = [func for func in dir(self) if callable(getattr(self, func)) and func.startswith('_do_')]
    # [/init]

    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        while interacting:
            try:
                command = self.read(f"{addr:06x} [{prompt}]> ")
                command = command.strip()
                if not command:
                    continue
                elif len(command.split()) == 1 and isinstance(command, str):
                    # Search according to name sequence first
                    for func_name in self.functions:
                        if func_name[4:].startswith(command):
                            chosen_function = func_name
                            break
                        else:
                            chosen_function = None
                    # Run the functions
                    for index, func_name in enumerate(self.functions):
                        if chosen_function != None:
                            print("Function Called: ", chosen_function)
                            interacting = getattr(self, chosen_function)(self.ip)
                            break
                        elif command in func_name:
                            print("Function Called: ",func_name)
                            interacting = getattr(self, func_name)(self.ip)
                            break
                        else:
                            if index == len(self.functions) - 1: 
                                self.write(f"Unknown command {command}")
                # elif command in self.handlers:
                #     interacting = self.handlers[command](self.ip)
                # If there is 2 text input
                elif len(command.split()) > 1 :
                    if len(command.split()) == 2:
                        first, second = command.split()
                        # if both input are addresses
                        if first.isdigit() and second.isdigit():
                            first, second = first.zfill(6), second.zfill(6)
                            self._do_show_memory_range(int(first), int(second))
                        # if first input is break/clear/add_watchpoint, second input is the address
                        if isinstance(first, str) and second.isdigit():
                            self.first_input = first
                            self.second_input = f"{int(second.zfill(6))}"
                            return True
                    else:
                        assert isinstance(command, int), "Memory address has to be an integer"
                        command = int(command.zfill(6))
                        self._do_show_memory_range(command)
                # elif command not in self.handlers:
                #     self.write(f"Unknown command {command}")
                # else:
                #     self.write("Unknown Error has occurred")
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
        return False
    # [/interact]

    def _do_show_memory_range(self, addr1, addr2 = None):
        assert addr1 < RAM_LEN, "First address out of range!"
        if addr2 != None:
            assert addr2 - addr1 <= RAM_LEN, "Out of RAM Range!"
            output = f"Address provided: {str(addr1)} {str(addr2)}\n"
            output += f"Value between this range of address: "
            for i in range(addr1, addr2):
                output += f"{self.ram[i]:06x} "
            self.write(output)
        else:
            output = f"Address provided: {str(addr1)}\n"
            output += f"Value of that address: {self.ram[addr1]:06x}"
            self.write(output)

    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, addr):
        self.show()
        return True
    # [/memory]

    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    # [step]
    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
    # [/step]


if __name__ == "__main__":
    VirtualMachineExtend.main()

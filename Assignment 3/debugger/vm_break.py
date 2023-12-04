import sys

from architecture import OPS, VMState
from vm_extend import VirtualMachineExtend


class VirtualMachineBreak(VirtualMachineExtend):
    # [init]
    def __init__(self):
        super().__init__()
        self.breaks = {}
        self.watchpoints = {}
        self.handlers |= {
            "b": self._do_add_breakpoint,
            "break": self._do_add_breakpoint,
            "c": self._do_clear_breakpoint,
            "clear": self._do_clear_breakpoint,
        }
        self.extended_functions = ["_do_add_breakpoint", "_do_clear_breakpoint", "_do_add_watchpoint"]
        self.watchpoint_triggered = False
    # [/init]

    # [show]
    def show(self):
        super().show()
        if self.breaks:
            self.write("-" * 6)
            for key, instruction in self.breaks.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")
        # TODO: Not really sure have to show watch points or not
        # if self.watchpoints:
        #     self.write("-" * 6)
        #     for key, instruction in self.watchpoints.items():
        #         self.write(f"{key:06x}: {self.disassemble(key, instruction)}")
    # [/show]

    # [run]
    def run(self):
        self.state = VMState.STEPPING
        while self.state != VMState.FINISHED:
            instruction = self.ram[self.ip]
            op, arg0, arg1 = self.decode(instruction)

            if len(self.watchpoints) != 0:
                for key, value in self.watchpoints.items():
                    original = f"{self.watchpoints[key]:06x}"
                    current = f"{self.ram[key]:06x}"
                    if original != current:
                        print(f"Changes detected at IP {self.ip:06x}")
                        # Halts the program
                        self.watchpoint_triggered = True
                        break
            
            if self.watchpoint_triggered:
                self.execute(1, 0, 0)
            # Reached the breakpoint and stop for another interaction
            if op == OPS["brk"]["code"]:
                original = self.breaks[self.ip]
                op, arg0, arg1 = self.decode(original)
                self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)

            else:
                if self.state == VMState.STEPPING:
                    # If return True, means only one of these 2 functions will be called
                    if self.interact(self.ip):
                        for func_name in self.extended_functions:
                            if func_name[4:].startswith(self.first_input):
                                chosen_function = func_name
                                break
                            else:
                                chosen_function = None
                        for index, func_name in enumerate(self.extended_functions):
                            if chosen_function != None:
                                print("Function Called: ", chosen_function)
                                interacting = getattr(self, chosen_function)(int(self.second_input))
                                break
                            elif self.first_input in func_name:
                                print("Function Called: ",func_name)
                                interacting = getattr(self, func_name)(int(self.second_input))
                                break
                            else:
                                if index == len(self.functions) - 1: 
                                    self.write(f"Unknown command {self.first_input}")

                self.ip += 1
                self.execute(op, arg0, arg1)
    # [/run]

    # [add]
    def _do_add_breakpoint(self, addr):
        if self.ram[addr] == OPS["brk"]["code"]:
            return
        self.breaks[addr] = self.ram[addr]
        self.ram[addr] = OPS["brk"]["code"]
        print(f"Added breakpoint at {addr:06x}")
        return True
    # [/add]

    # [clear]
    def _do_clear_breakpoint(self, addr):
        if self.ram[addr] != OPS["brk"]["code"]:
            return
        self.ram[addr] = self.breaks[addr]
        del self.breaks[addr]
        print(f"Cleared breakpoint at {addr:06x}")
        return True
    
    def _do_add_watchpoint(self, addr):
        # It should store the original address value
        self.watchpoints[addr] = self.ram[addr]
        print(f"Added watchpoint at {str(self.second_input)}")
        return True
    # [/clear]

if __name__ == "__main__":
    VirtualMachineBreak.main()

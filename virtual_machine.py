class VirtualMachine:
    def __init__(self, bytecodes, ram_size=256, executing=True):
        self.bytecodes = bytecodes
        self.data = [None]*ram_size
        self.stack = []
        self.executing = executing
        self.pc = 0

    def push(self, value):
        """Push something onto the stack."""
        self.stack += [value]

    def pop(self):
        """Pop something from the stack. Crash if empty."""
        return self.stack.pop()

    def read_memory(self, index):
        """Read from memory, crashing if index is out of bounds."""
        return self.data[index]

    def write_memory(self, index, value):
        """Write to memory.  Crash if index is out of bounds."""
        self.data[index] = value

    def run(self):
        while self.executing:
            increment = self.bytecodes[self.pc].autoincrement
            self.bytecodes[self.pc].execute(self)
            if increment:
                self.pc += 1


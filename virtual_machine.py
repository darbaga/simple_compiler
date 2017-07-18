class VirtualMachine:
    def __init__(self, bytecodes, ram_size=256, stack_size=32, executing=True):
        self.bytecodes = bytecodes
        self.data = [None]*ram_size
        self.stack = [None]*stack_size
        self.stack_size = stack_size
        self.stack_top = 0
        self.executing = executing
        self.pc = 0

    def push(self, value):
        """Push something onto the stack."""
        if self.stack_top+1 > self.stack_size:
            raise IndexError
        self.stack[self.stack_top] = value
        self.stack_top += 1

    def pop(self):
        """Pop something from the stack. Crash if empty."""
        if self.stack_top == 0:
            raise IndexError
        self.stack_top -= 1
        return self.stack.pop(self.stack_top)

    def read_memory(self, index):
        """Read from memory, crashing if index is out of bounds."""
        return self.data[index]

    def write_memory(self, index, value):
        """Write to memory.  Crash if index is out of bounds."""
        self.data[index] = value

    def run(self):
        while self.executing:
            self.bytecodes[self.pc].execute(self)
            if self.bytecodes[self.pc].autoincrement:
                self.pc += 1


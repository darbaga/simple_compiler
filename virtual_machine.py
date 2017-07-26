class VirtualMachine:
    def __init__(self, ram_size=512, executing=True):
        self.data = {i: None for i in range(ram_size)}
        self.stack = []
        self.executing = executing
        self.pc = 0
        self.devices_start = 256

    def push(self, value):
        """Push something onto the stack."""
        self.stack += [value]

    def pop(self):
        """Pop something from the stack. Crash if empty."""
        return self.stack.pop()

    def read_memory(self, index):
        """Read from memory, crashing if index is out of bounds."""
        if isinstance(self.data[index], DeviceProxy):
            return self.data[index].read(index)
        else:
            return self.data[index]

    def write_memory(self, index, value):
        """Write to memory.  Crash if index is out of bounds."""
        if isinstance(self.data[index], DeviceProxy):
            self.data[index].write(index, value)
        else:
            self.data[index] = value

    def register_device(self, device, needed_addresses):
        """Given an instantiated device and the number of required addresses, registers it in memory"""
        # If not enough addresses, just error out
        if self.devices_start+needed_addresses > len(self.data):
            raise Exception('Not enough addresses to allocate')
        proxyed_device = DeviceProxy(device, self.devices_start)
        for i in range(self.devices_start, self.devices_start+needed_addresses):
            self.data[i] = proxyed_device
        self.devices_start += needed_addresses

    def run(self, bytecodes):
        self.bytecodes = bytecodes
        while self.executing:
            increment = self.bytecodes[self.pc].autoincrement
            self.bytecodes[self.pc].execute(self)
            if increment:
                self.pc += 1


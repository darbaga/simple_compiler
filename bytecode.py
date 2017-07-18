class BytecodeBase:
    autoincrement = True # For jump
    
    def __init__(self):
        # Eventually might want to add subclassed bytecodes here
        # Though __subclasses__ works quite well
        pass

    def execute(self, machine):
        pass


class Push(BytecodeBase):
    def __init__(self, data):
        self.data = data

    def execute(self, machine):
        machine.push(self.data)

class Pop(BytecodeBase):
    def execute(self, machine):
        return machine.pop()

class ReadMemory(BytecodeBase):
    def __init__(self, index):
        self.index = index

    def execute(self, machine):
        return machine.read_memory(self.index)

class WriteMemory(BytecodeBase):
    def __init__(self, index, value):
        self.index, self.value = index, value

    def execute(self, machine):
        machine.write_memory(self.index, self.value)


class Add(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(a+b)

class Sub(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(a-b)

class Mul(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(a*b)

class Div(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(a/b)

class Terminate(BytecodeBase):
    def execute(self, machine):
        machine.executing = False

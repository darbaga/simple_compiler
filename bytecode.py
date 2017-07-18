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
        machine.push(machine.read_memory(self.index))

class WriteMemory(BytecodeBase):
    def __init__(self, index, value):
        self.index, self.value = index, value

    def execute(self, machine):
        machine.write_memory(self.index, self.value)


class Add(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(b+a)

class Sub(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(b-a)

class Mul(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(b*a)

class Div(BytecodeBase):
    def execute(self, machine):
        a = machine.pop()
        b = machine.pop()
        machine.push(b/a)


class Terminate(BytecodeBase):
    def execute(self, machine):
        machine.executing = False

class Jump(BytecodeBase):
    def __init__(self, jump_to):
        self.autoincrement = False
        self.jump_to = jump_to

    def execute(self, machine):
        machine.pc = self.jump_to

class ConditionalJump(BytecodeBase):
    def __init__(self, value, jump_to):
        self.autoincrement = False
        self.value = value
        self.jump_to = jump_to

    def execute(self, machine):
        val = machine.pop()
        machine.push(val)
        if val == self.value:
            machine.pc = self.jump_to
        else:
            machine.pc += 1


class Print(BytecodeBase):
    def execute(self, machine):
        val = machine.pop()
        machine.push(val)
        print(val)

class WriteTop(BytecodeBase):
    def __init__(self, index):
        # We need this because we can't layer bytecodes
        # WriteMemory(Pop()) Fails because only WriteMemory gets executed
        self.index = index

    def execute(self, machine):
        machine.write_memory(self.index, machine.pop())

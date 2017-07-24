from virtual_machine import VirtualMachine
from bytecode import *

bytecode_table = {
    'Push': Push,
    'Pop': Pop,
    'ReadMemory': ReadMemory,
    'WriteMemory': WriteMemory,
    'Add': Add,
    'Sub': Sub,
    'Mul': Mul,
    'Div': Div,
    'Terminate': Terminate,
    'Jump': Jump,
    'ConditionalJump': ConditionalJump,
    'Print': Print,
    'WriteTop': WriteTop
}

def assemble(string):
    # Strip newlines, then split at space
    string = string.splitlines()
    string = [i.split(' ') for i in string]
    bytecodes = []
    for i in string:
        instruction = bytecode_table[i[0]]
        args = [int(j) for j in i[1:]] # Our instructions expect ints
        if len(args) < instruction.num_args:
            # Todo actual error handling
            raise Exception('Insufficient arguments')
        elif len(args) > instruction.num_args:
            raise Exception('Too many arguments')
        else:
            bytecodes.append(instruction(*args))
    f=VirtualMachine(bytecodes)
    f.run()

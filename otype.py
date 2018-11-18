def run_o(otype):

    code  = o.type.split()

    if code [0] == "halt" :
        opcode == "110"
    elif code [0] == "noop" :
        opcode == "111"

    notuse= "0000000000000000000000"  
    machine = "\t" + opcode + "\t" + notuse 
    print(machine)
    return machine


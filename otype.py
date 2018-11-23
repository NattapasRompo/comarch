def run_o(otype):

    code  = otype.split()
    opcode=""
    change=""
    if code [0] == "noop" :
        opcode = "111"
    elif code [0] == "halt" or code[1] == "halt" :
        opcode = "110"
    

    notuse= "0000000000000000000000"  
    machine = "\t" + opcode + "\t" + notuse 
    change = opcode+notuse
    #print(machine)
    #print(int(change,2))
    return int(change,2)


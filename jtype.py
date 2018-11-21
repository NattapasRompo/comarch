
def run_j(jtype):
    code  = jtype.split()
    opcode = "101"
    machine=""
    if code[0] == "jalr":
        regA = bin(int(code[1]))[2:].zfill(3)
        regB = bin(int(code[2]))[2:].zfill(3)
        notuse= "0000000000000000"
        machine = "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + notuse

    elif code[0] != "jalr" and code[1] == "jalr" :
        regA = bin(int(code[2]))[2:].zfill(3)
        regB = bin(int(code[3]))[2:].zfill(3)
        notuse= "0000000000000000"
        machine = code[0] + "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + notuse

    print(machine)
    return machine
     
    
    
    
    
    
    
    


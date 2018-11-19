def run_i(itype):
    code  = itype.split()
    opcode=""
    if code[0] == "lw" or "sw" or "beq":
        if code[0] == "lw":
            opcode == "010"
            
        elif code[0] == "sw":
            opcode == "011"
            
        elif code[0] == "beq":
            opcode == "100"
        
    regA = bin(int(code[1]))[2:].zfill(3)
    regB = bin(int(code[2]))[2:].zfill(3)
    offset=""
    if code[3].isdigit() :
        offset = bin(int(code[3]))[2:].zfill(16)
    else :
        offset = code[3]
    

    #if code [3] == not finish
    machine = "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + offset

    print(machine)
    return machine


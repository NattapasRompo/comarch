def run_i(itype):
    code  = itype.split()
    opcode=""

    machine=""
    
    

    
    if (code[0] == "lw" or code[0] == "sw" or code[0] == "beq") and (code[1] != "lw" or code[1] != "sw" or code[1] != "beq") :
        
        if code[0] == "lw" :
            opcode = "010"
           
            
        elif code[0] == "sw" :
            opcode = "011"
            
        elif code[0] == "beq" :
            opcode = "100"
        
        regA = bin(int(code[1]))[2:].zfill(3)
        regB = bin(int(code[2]))[2:].zfill(3)
        offset=""
        if code[3].isdigit() :
            offset = bin(int(code[3]))[2:].zfill(16)
        else :
            offset = code[3]
        
        machine = "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + offset
        
    elif (code[0] != "lw" or code[0] != "sw" or code[0] != "beq") and (code[1] == "lw" or code[1] == "sw" or code[1] == "beq") :
        if code[1] == "lw" :
            opcode = "010"
            
        elif code[1] == "sw" :
            opcode = "011"
            
        elif code[1] == "beq" :
            opcode = "100"
        regA = bin(int(code[2]))[2:].zfill(3)
        regB = bin(int(code[3]))[2:].zfill(3)
        offset=""
        if code[4].isdigit() :
            offset = bin(int(code[4]))[2:].zfill(16)
        else :
            offset = code[4]
        machine = code[0] + "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + offset

    

    print(machine)
    return machine


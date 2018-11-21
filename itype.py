def run_i(itype):
    code  = itype.split()
    opcode=""
    machine=""
    change=""
    
    

    
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
           if int(code[3])<0 :
                offset = (bin(int(code[3])&0b1111111111111111))[2:].zfill(16)
        machine = "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + offset
        change = opcode+regA+regB+offset
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
            if int(code[4])<0 :
                offset = (bin(int(code[4])&0b1111111111111111))[2:].zfill(16)
        machine = code[0] + "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + offset
        change = opcode+regA+regB+offset
    

    #print(machine)
    print(int(change,2))
    return int(change,2)


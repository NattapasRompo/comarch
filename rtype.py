def run_r(rtype):
    #print(rtype)
    code  = rtype.split()
    opcode = ""
    change=""
   
    
    if code[0] == "add" or code[0] == "nand"   :
        if code [0] == "add":
            opcode = "000"
        elif code [0] == "nand":
            opcode = "001"
    
        regA = bin(int(code[1]))[2:].zfill(3)
        regB = bin(int(code[2]))[2:].zfill(3)
        if code [3].isdigit:
            destreg = bin(int(code[3]))[2:].zfill(3)
        else :
            destreg = code[3]
        notuse= "0000000000000"
        machine = "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + notuse + "\t" +destreg 
        change = opcode+regA+regB+notuse+destreg

    elif code[0] != "add" or "nand" and code[1] == "add" or "nand" :
        if code [1] == "add":
            opcode = "000"
        elif code [1] == "nand":   
            opcode = "001"
        regA = bin(int(code[2]))[2:].zfill(3)
        regB = bin(int(code[3]))[2:].zfill(3)
        if code [4].isdigit :
            destreg = bin(int(code[4]))[2:].zfill(3)
        else :
            destreg = code[4]
        notuse= "0000000000000"
        machine = code[0] +"\t" + opcode + "\t" + regA + "\t" + regB + "\t" + notuse + "\t" +destreg 
        change = opcode+regA+regB+notuse+destreg
    
    #print(machine)
    #print(int(change,2))
    return int(change,2)
def run_r(rtype):
    print(rtype)
    code  = rtype.split()
    print(code[0])
    print(code[1])
    if code [0] == "and" :
        opcode == "000"
    elif code [0] == "nand" :
        opcode == "001"

    #if code[0] == "and" or  "nand"   :
    regA = bin(int(code[1]))[2:].zfill(3)
    regB = bin(int(code[2]))[2:].zfill(3)
    notuse= "0000000000000000"
    machine = "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + notuse
    """
    elif code[0] != "jalr" and code[1] == "jalr" :
        regA = bin(int(code[2]))[2:].zfill(3)
        regB = bin(int(code[3]))[2:].zfill(3)
        notuse= "0000000000000000"
        machine = code[0] + "\t" + opcode + "\t" + regA + "\t" + regB + "\t" + notuse
    """
    print(machine)
    return machine
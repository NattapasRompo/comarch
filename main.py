#jalr 4 2->x0=pc+4 , x1=pc+imm
def machine (order):
   
   if order == "add": 
       opcode = "000"
   elif order == "nand": 
       opcode = "001"
   elif order == "lw": 
       opcode = "010"
   elif order == "sw": 
       opcode = "011"
   elif order == "beq": 
       opcode = "100"
   elif order == "jalr": 
       opcode = "101"   
   elif order == "halt": 
       opcode = "110"
   elif order == "noop": 
       opcode = "111"
   return opcode

def run_rtype(rtype):
    label,order,rd,rs,rt = rtype.split( )
    
    type = machine(order) 
    regA = bin(int(rs))[2:].zfill(3)
    regB = bin(int(rt))[2:].zfill(3)
    destreg = bin(int(rd))[2:].zfill(3)
    notuse= "0000000000000"
    code = label+" "+type+" "+regA+" "+regB+" "+notuse+" "+destreg
    print (code)

def run_itype(itype):
    label,order,rs,rt,address = itype.split( )
    
    type = machine(order) 
    regA = bin(int(rs))[2:].zfill(3)
    regB = bin(int(rt))[2:].zfill(3)
    notuse= "0000000000000000"
    code = label+" "+type+" "+regA+" "+regB+" "+notuse
    print (code)   

def run_jtype(jtype):
    label,order,rs,rd = jtype.split( )
    
    type = machine(order) 
    regA = bin(int(rs))[2:].zfill(3)
    regB = bin(int(rd))[2:].zfill(3)
    notuse= "0000000000000000"
    code = label+" "+type+" "+regA+" "+regB+" "+notuse
    print (code)

def run_otype(otype):
    label,order = otype.split( )
    
    type = machine(order) 
    notuse= "0000000000000000000000"
    code = label+" "+type+" "+notuse
    print (code)

 #def runcode (allcode):
        #A= ตัดบรรทัด allcode
 #   label =a.split( )

 #   if label[0] or label[1] == "and" or "nand":
   #     run_rtype(a)
  #  elif label[1] == "lw" or "sw" or "beq":
    #    run_itype(a)
    #elif label[1] == "jalr":
   #     run_jtype(a)
    #elif label[1] = "halt" or "noop":
     #   run_otype(a)   

run_jtype("start jalr 4 3")
run_itype("       lw 1 2 3")









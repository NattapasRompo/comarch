import jtype as j_ty
import itype as i_ty
import rtype as r_ty
import otype as o_ty    
#jalr 4 2->x0=pc+4 , x1=pc+imm
def findlabel(la,numl,namel):
    j=0
    for i in namel:
        if la == i: return j
        j+=1
    return -9999

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def BehavSimulate (maccode):
        memory=[]
        reg=[0,0,0,0,0,0,0,0]
        ishalt=False
        pc=0
        
        memory=maccode.readlines()
        for x in range(len(memory)):
                 print("memmory [" + str(x) + "] = "+str(memory[x]) )

        while 1 :
                
                print("state "+"PC "+str(pc))

                binary=bin(int(memory[pc]))[2:].zfill(32)
                # print(binary)
                opcode=binary[7:10] #bit 24-22 
                regA=binary[10:13] #bit 24-22 
                regB=binary[13:16] #bit 24-22 
                rd=binary[29:32] #bit 24-22 

                indA=int(binary[10:13],2)  #bit 21-19
                indB=int(binary[13:16],2)  #bit 18-16
                indrd=int(binary[29:32],2)    #bit 2-0
                if  binary[16] == "1" :
                    offsetField=int(binary[16:32],2)-(1<<16)
                else :
                    offsetField=int(binary[16:32],2)

                # print(offsetField)

                if(opcode == "000"): #and
                        reg[indrd]=reg[indA]+reg[indB]  
                        pc+=1                 
                elif opcode == "001": #Nand
                        reg[indrd]=not (reg[indA] and reg[indB])
                        pc+=1   
                elif opcode == "010": #lw
                        reg[indB]=int(memory[reg[indA]+offsetField])
                        pc+=1   
                elif opcode == "011": #sw
                        memory[reg[indA]+offsetField]=str(reg[indB])
                        pc+=1   
                elif opcode == "100": #beq
                        if reg[indA] == reg[indB]:
                            pc=pc+offsetField+1 
                        else: pc=pc+1
                elif opcode == "101": #jalr
                        if reg[indA]==reg[indB]:
                                reg[indB]=pc+1
                                pc=pc+1
                        else:
                                reg[indB]=pc+1
                                pc=reg[indA]
                elif opcode =="110":
                    ishalt=True
                    pc+=1   
                    break
                else : pc+=1
              
                print("reg :")
                for x in range(len(reg)) :
                       print("reg[" + str(x) + "] = "+str(reg[x]) )    
                print("-------------------------------------------") 
                # print("opcode = ",opcode," reg A = ",regA," reg B = ",regB," rd = ",rd) 


BehavSimulate(open('test1.txt'))

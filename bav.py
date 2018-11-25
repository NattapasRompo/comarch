import jtype as j_ty
import itype as i_ty
import rtype as r_ty
import otype as o_ty    
 
memory=[]
reg=[0,0,0,0,0,0,0,0]
count=0
pc=0  
 
 
def findlabel(la,numl,namel):
    j=0
    for i in namel:
        if la == i: return j
        j+=1
    return -9999
                       # return positive value as is
def printState():
        global memory
        global reg
        global count
        global pc
 
        print("@@@")
        print("state ")
        print("PC "+str(pc))
        print("memmory :")
        for x in range(len(memory)):
                print("         memmory [" + str(x) + "] = "+str(memory[x]) )      
        print("reg :")
        for x in range(len(reg)) :
                print("          reg[" + str(x) + "] = "+str(reg[x]) )    
        print("end state")
       
 
 
 
def BehavSimulate (maccode):
        global memory
        global reg
        global count
        global pc
 
        memory=maccode.readlines()
        for x in range(len(memory)):
                 print("         memmory [" + str(x) + "] = "+str(memory[x]) )
 
        while 1 :
                count+=1 #total instruction              
                binary=bin(int(memory[pc]))[2:].zfill(32)
                opcode=binary[7:10] #bit 24-22
                indA=int(binary[10:13],2)  #bit 21-19
                indB=int(binary[13:16],2)  #bit 18-16
                indrd=int(binary[29:32],2)    #bit 2-0
                if  binary[16] == "1" :
                    offsetField=int(binary[16:32],2)-(1<<16)
                else :
                    offsetField=int(binary[16:32],2)
 
                if(opcode == "000"): #and
                        reg[indrd]=reg[indA]+reg[indB]  
                        pc+=1                
                elif opcode == "001": #Nand
                        reg[indrd]= ~ (reg[indA] & reg[indB])
                        pc+=1  
                elif opcode == "010": #lw
                        try :
                                reg[indB]=int(memory[reg[indA]+offsetField])
                                pc+=1
                        except IndexError :
                                print("index ")  
                elif opcode == "011": #sw
                        if(reg[indA]+offsetField>len(memory)-1) :
                                memory.append(str(reg[indB]))
                        else:                                
                                memory[reg[indA]+offsetField]=str(reg[indB])
                        pc+=1  
                elif opcode == "100": #beq
                        if reg[indA] == reg[indB]:
                            pc=pc+offsetField+1
                        else: pc=pc+1
                elif opcode == "101": #jalr
                        if indA==indB:
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
                printState()
        print("machine halted total of "+str(count)+" instructions executed final state of machine:")
        printState()
 
 
BehavSimulate(open('Output.txt'))
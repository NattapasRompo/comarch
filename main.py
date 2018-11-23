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

def BehavSimulate (maccode):
        memory=[]
        reg=[0,0,0,0,0,0,0,0]
        ishalt=False
        pc=0
        
        memory=maccode.readlines()
        for x in range(len(memory)):
                 print("memmory [" + str(x) + "] = "+str(memory[x]) )

        while 1 :
                
                print("state")
                print("PC "+str(pc))

                binary=bin(int(memory[pc]))[2:].zfill(32)
                print(binary)
                opcode=binary[7:10] #bit 24-22 
                regA=binary[10:13] #bit 24-22 
                regB=binary[13:16] #bit 24-22 
                rd=binary[29:32] #bit 24-22 

                indA=int(binary[10:13],2)  #bit 21-19
                indB=int(binary[13:16],2)  #bit 18-16
                indrd=int(binary[29:32],2)    #bit 2-0
                offsetField=int(binary[16:32],2)



                if(opcode == "000"): #and
                        reg[indrd]=reg[indA]+reg[indB]  
                        pc+=1                 
                elif opcode == "001": #Nand
                        reg[indrd]=~(reg[indA]&reg[indB])
                        pc+=1   
                elif opcode == "010": #lw
                        reg[indB]=int(memory[reg[indA]+offsetField])
                        pc+=1   
                elif opcode == "011": #sw
                        memory[reg[indA]+offsetField]=str(reg[indB])
                        pc+=1   
                elif opcode == "100": #beq
                        if reg[indA] == regB[indB]:
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
                
                
                # print("memmory :")
                # for x in range(len(memory)) :
                #        print("memmory [" + str(x) + "] = "+str(memory[x]) )
                
                print("reg :")
                for x in range(len(reg)) :
                       print("memmory [" + str(x) + "] = "+str(reg[x]) )     
                print("opcode = ",opcode," reg A = ",regA," reg B = ",regB," rd = ",rd) 

                   

    



# def runcode (allcode):
#     lineall=allcode.readlines()
#     count = 0
#     count2 = 0
#     numline=[] 
#     nameline=[]
#     for j in lineall:
#         line =j.split()
#         if line[0] != "add" and line[0] != "nand" and line[0] != "lw"  and line[0] != "sw" and line[0] != "beq" and line[0] !="jalr" and line[0] != "halt" and line[0] != "noop":
#             #print("----------------------------------------------------------")
#             #print(count)
#             #print(line[0])
#             numline.append(count)
#             nameline.append(line[0])
#             count2 += 1
#             #print("----------------------------------------------------------")
          #count += 1

    

#     #print(allcode)  
#     for i in lineall:
#         label =i.split()
#         try:
#             if label[3].isdigit() : gotdata = 'null' 
#             else : #print(findlabel(label[3],numline,nameline))
#                 if numline[findlabel(label[3],numline,nameline)] != -9999 :
#                     print(numline[findlabel(label[3],numline,nameline)])
#                     label[3]=str(numline[findlabel(label[3],numline,nameline)])
#                     i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]
#                 else:
#                     print("exit(0)")
#             if label[4].isdigit() : gotdata = 'null' 
#             else : #print(findlabel(label[4],numline,nameline))
#                 if numline[findlabel(label[5],numline,nameline)] != -9999 :
#                     print(numline[findlabel(label[4],numline,nameline)])
#                     label[4]=str(numline[findlabel(label[4],numline,nameline)])
#                     i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]+"\t"+label[4]
#                 else : 
#                     print("exit(0)")
#             if label[5].isdigit() : gotdata = 'null' 
#             else : #print(findlabel(label[5],numline,nameline))
#                 if numline[findlabel(label[5],numline,nameline)] != -9999 :
#                     print(numline[findlabel(label[5],numline,nameline)])
#                     label[5]=str(numline[findlabel(label[5],numline,nameline)])
#                     i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]+"\t"+label[4]+"\t"+label[5]
#                 else:
#                     print("exit(0)")
            
#         except IndexError:
#             gotdata = 'null'        

#     #for i in lineall:
#         #print(i)
#         #label =i.split()
#         if label[0]  == "halt" or label[0]  == "noop" or label[1] == "halt":
#             o_ty.run_o(i)
#         elif (label[0] == "add" or label[1] == "add") or (label[0] == "nand" or label[1] == "nand"):
#             r_ty.run_r(i)
#         elif (label[0] == "lw" or label[1] == "lw") or (label[0] == "sw" or label[1] == "sw") or (label[0] == "beq" or label[1] == "beq"):
#             i_ty.run_i(i)
#         elif label[0] or label[1]  == "jalr":
#             j_ty.run_j(i)
#         else:
#             break   
# #j_ty.run_j("start  jalr  4  3")
# runcode(open('test.txt'))
BehavSimulate(open('text1.txt'))





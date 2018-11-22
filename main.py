import jtype as j_ty
import itype as i_ty
import rtype as r_ty
import otype as o_ty   
import fill as fill_ty 
#jalr 4 2->x0=pc+4 , x1=pc+imm
def findlabel(la,namel):
    j=0
    for i in namel:
        if la == i: return j
        j+=1
    return -9999 

def findoffset(i,numline,nameline,countline):
    label =i.split()
    try:
        if label[3].isdigit() : gotdata = 'null' 
        else : 
            if numline[findlabel(label[3],nameline)] != -9999 :
                #print(numline[findlabel(label[3],nameline)])
                if label[0] == "beq" or label[1] == "beq":
                    label[3]=str(numline[findlabel(label[3],nameline)]-1-countline)
                else :
                    label[3]=str(numline[findlabel(label[3],nameline)])
                i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]
            else:
                print("exit(1)")

        if label[4].isdigit() : gotdata = 'null' 
        else : 
            if numline[findlabel(label[5],nameline)] != -9999 :
                #print(numline[findlabel(label[4],nameline)])
                if label[0] == "beq" or label[1] == "beq":
                    label[4]=str(numline[findlabel(label[4],nameline)]-1-countline)
                else :
                    label[4]=str(numline[findlabel(label[4],nameline)])
                i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]+"\t"+label[4]
            else : 
                print("exit(1)")

        if label[5].isdigit() : gotdata = 'null' 
        else : 
            if numline[findlabel(label[5],nameline)] != -9999 :
                #print(numline[findlabel(label[5],nameline)])
                if label[0] == "beq" or label[1] == "beq":
                    label[5]=str(numline[findlabel(label[5],nameline)]-1-countline)
                else :
                    label[5]=str(numline[findlabel(label[5],nameline)])
                i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]+"\t"+label[4]+"\t"+label[5]
            else:
                print("exit(1)")       
    except IndexError:
            gotdata = 'null'        
    return i


def runcode (allcode):
    lineall=allcode.readlines()
    count = 0
    count2 = 0
    numline=[] 
    nameline=[]
    for j in lineall:
        line =j.split()
        
        if line[0] != "add" and line[0] != "nand" and line[0] != "lw"  and line[0] != "sw" and line[0] != "beq" and line[0] !="jalr" and line[0] != "halt" and line[0] != "noop":
            #print("----------------------------------------------------------")
            #print(count)
            #print(line[0])
            numline.append(count)
            nameline.append(line[0])
            count2 += 1
            #print("----------------------------------------------------------")
        count += 1
    

    #print(allcode)  
    countline=0
    for i in lineall:
        label =i.split()
        i=findoffset(i,numline,nameline,countline)    

        if label[0]  == "halt" or label[0]  == "noop" or label[1] == "halt":
            o_ty.run_o(i)
        elif label[1] == ".fill" :
            fill_ty.run_fill(i)
        elif (label[0] == "add" or label[1] == "add") or (label[0] == "nand" or label[1] == "nand"):
            r_ty.run_r(i)
        elif (label[0] == "lw" or label[1] == "lw") or (label[0] == "sw" or label[1] == "sw") or (label[0] == "beq" or label[1] == "beq"):
            i_ty.run_i(i)
        elif label[0] or label[1]  == "jalr":
            j_ty.run_j(i)
        
        else:
            break   
        countline+=1


#j_ty.run_j("start  jalr  4  3")
runcode(open('test.txt'))

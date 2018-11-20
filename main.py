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

def runcode (allcode):
    lineall=allcode.readlines()
    count = 0
    count2 = 0
    numline=[] 
    nameline=[]
    for j in lineall:
        line =j.split()
        count += 1
        if line[0] != "add" and line[0] != "nand" and line[0] != "lw"  and line[0] != "sw" and line[0] != "beq" and line[0] !="jalr" and line[0] != "halt" and line[0] != "noop":
            #print("----------------------------------------------------------")
            #print(count)
            #print(line[0])
            numline.append(count)
            nameline.append(line[0])
            count2 += 1
            #print("----------------------------------------------------------")

    

    #print(allcode)  
    for i in lineall:
        label =i.split()
        try:
            if label[3].isdigit() : gotdata = 'null' 
            else : #print(findlabel(label[3],numline,nameline))
                if numline[findlabel(label[3],numline,nameline)] != -9999 :
                    print(numline[findlabel(label[3],numline,nameline)])
                    label[3]=numline[findlabel(label[3],numline,nameline)]
                else:
                    print("exit(0)")
            if label[4].isdigit() : gotdata = 'null' 
            else : #print(findlabel(label[4],numline,nameline))
                if numline[findlabel(label[5],numline,nameline)] != -9999 :
                    print(numline[findlabel(label[4],numline,nameline)])
                    label[4]=numline[findlabel(label[4],numline,nameline)]
                else : 
                    print("exit(0)")
            if label[5].isdigit() : gotdata = 'null' 
            else : #print(findlabel(label[5],numline,nameline))
                if numline[findlabel(label[5],numline,nameline)] != -9999 :
                    print(numline[findlabel(label[5],numline,nameline)])
                    label[5]=numline[findlabel(label[5],numline,nameline)]
                else:
                    print("exit(0)")
        except IndexError:
            gotdata = 'null'        

"""
    for i in lineall:
        #print(i)
        label =i.split()
        if label[0]  == "halt" or label[0]  == "noop" or label[1] == "halt":
            o_ty.run_o(i)
        elif (label[0] == "add" or label[1] == "add") or (label[0] == "nand" or label[1] == "nand"):
            r_ty.run_r(i)
        elif (label[0] == "lw" or label[1] == "lw") or (label[0] == "sw" or label[1] == "sw") or (label[0] == "beq" or label[1] == "beq"):
            i_ty.run_i(i)
        elif label[0] or label[1]  == "jalr":
            j_ty.run_j(i)
        else:
            break   
     """

#j_ty.run_j("start  jalr  4  3")
runcode(open('test.txt'))
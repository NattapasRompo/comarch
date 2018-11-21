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
        if label[2].isdigit() : gotdata = 'null' 
        else : 
            if numline[findlabel(label[2],nameline)] != -9999 :
                #print(numline[findlabel(label[5],nameline)])
                if label[1] == ".fill":
                    label[2]=str(numline[findlabel(label[2],nameline)])
                i=label[0]+"\t"+label[1]+"\t"+label[2]
            else:
                print("exit(1)") 
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
    txt=""
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
            txt = txt + str(o_ty.run_o(i)) +"\n"
        elif label[1] == ".fill" :
            txt = txt + str(fill_ty.run_fill(i))+"\n"
        elif (label[0] == "add" or label[1] == "add") or (label[0] == "nand" or label[1] == "nand"):
            txt = txt + str(r_ty.run_r(i))+"\n"
        elif (label[0] == "lw" or label[1] == "lw") or (label[0] == "sw" or label[1] == "sw") or (label[0] == "beq" or label[1] == "beq"):
            txt = txt + str(i_ty.run_i(i))+"\n"
        elif label[0] or label[1]  == "jalr":
            txt = txt + str(j_ty.run_j(i))+"\n"
        else:
            break   
        countline+=1
    
    return txt


#j_ty.run_j("start  jalr  4  3")

#print(runcode(open('test.txt')))
text_file = open("Output.txt", "w")
text_file.write(runcode(open('test.txt')))
text_file.close()
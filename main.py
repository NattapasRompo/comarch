import jtype as j_ty
import itype as i_ty
import rtype as r_ty
import otype as o_ty   
import fill as fill_ty 
import sys
#jalr 4 2->x0=pc+4 , x1=pc+imm
def findsameLabel(nameline):
    i=0
    while(i<len(nameline)):
        j=i+1
        while (j < len(nameline)) :
            if nameline[i] == nameline[j] : sys.exit("exit(1)")
            j+=1
        i=i+1

def findlabel(la,namel,isfill):
    j=0
    err=99999
    for i in namel:
        if la == i: return j
        j+=1
    if isfill != 2 :
        sys.exit("exit(1)")
    else : return 99999

def findoffset(i,numline,nameline,countline):
    label =i.split()
    try:
        if label[2].isdigit() == False :
            if numline[findlabel(label[2],nameline,2)] != 99999 :
                if label[1] == ".fill":
                    label[2]=str(numline[findlabel(label[2],nameline,2)])
                i=label[0]+"\t"+label[1]+"\t"+label[2]


        elif label[3].isdigit() == False :
            if label[0] == "beq" or label[1] == "beq" :
                label[3]=str(numline[findlabel(label[3],nameline,3)]-1-countline)
            elif label[0] == "lw" or label[1] == "lw" or label[0] == "sw" or label[1] == "sw" :
                label[3]=str(numline[findlabel(label[3],nameline,3)]-int(label[1]))
            else :
                label[3]=str(numline[findlabel(label[3],nameline,3)])
            i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]

                

        elif label[4].isdigit() == False :
            if label[0] == "beq" or label[1] == "beq" :
                label[4]=str(numline[findlabel(label[4],nameline,4)]-1-countline)
            elif label[0] == "lw" or label[1] == "lw" or label[0] == "sw" or label[1] == "sw" :
                label[4]=str(numline[findlabel(label[4],nameline,4)]-int(label[2]))
            else :
                label[4]=str(numline[findlabel(label[4],nameline,4)])
            i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]+"\t"+label[4]


        elif label[5].isdigit() == False :
            if label[0] == "beq" or label[1] == "beq" :
                label[5]=str(numline[findlabel(label[5],nameline,5)]-1-countline)
            elif label[0] == "lw" or label[1] == "lw" or label[0] == "sw" or label[1] == "sw":
                label[5]=str(numline[findlabel(label[5],nameline,5)]-int(label[3]))
            else :
                label[5]=str(numline[findlabel(label[5],nameline,5)])
            i=label[0]+"\t"+label[1]+"\t"+label[2]+"\t"+label[3]+"\t"+label[4]+"\t"+label[5]
                

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
            numline.append(count)
            nameline.append(line[0])
            #print(count)
            #print(line[0])
            #print("---------------")
            count2 += 1
        count += 1
        
    findsameLabel(nameline)
    
    #print(allcode)  
    countline=0
    for i in lineall:
        #print(i)
        label =i.split()
        i=findoffset(i,numline,nameline,countline)    
        print(i)
        if label[0]  == "halt" or label[0]  == "noop" or label[1] == "halt":
            txt = txt + str(o_ty.run_o(i)) +"\n"
        elif label[1] == ".fill" :
            txt = txt + str(fill_ty.run_fill(i))+"\n"
        elif label[0] == "add" or label[1] == "add" or label[0] == "nand" or label[1] == "nand":
            txt = txt + str(r_ty.run_r(i))+"\n"
        elif label[0] == "lw" or label[1] == "lw" or label[0] == "sw" or label[1] == "sw" or label[0] == "beq" or label[1] == "beq":
            txt = txt + str(i_ty.run_i(i))+"\n"
        elif label[0] == "jalr" or label[1]  == "jalr":
            txt = txt + str(j_ty.run_j(i))+"\n"
        else:
            sys.exit("exit(1)")  
        countline+=1
 
    return txt


#j_ty.run_j("start  jalr  4  3")

#runcode(open('test.txt'))
text_file = open("Output.txt", "w")
text_file.write(runcode(open('com.txt')))
text_file.close()
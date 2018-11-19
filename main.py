import jtype as j_ty
import itype as i_ty
import rtype as r_ty
import otype as o_ty    
#jalr 4 2->x0=pc+4 , x1=pc+imm
def runcode (allcode):
    for i in allcode.readlines():
        print(i)
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
     
#j_ty.run_j("start  jalr  4  3")
runcode(open('test.txt'))

#run_itype("       lw 1 2 3")
#Teatgit







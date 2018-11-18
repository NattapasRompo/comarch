import jtype as j_ty
import itype as i_ty
import rtype as r_ty
import otype as o_ty
#jalr 4 2->x0=pc+4 , x1=pc+imm
def runcode (allcode):
    for i in allcode.readlines():
        print(i)
        label =i.split()
        if label[0] or label[1] == "and" or "nand":
            r_ty.run_r(i)
        elif label[0] or label[1]   == "lw" or "sw" or "beq":
            i_ty.run_i(i)
        elif label[0] or label[1]  == "jalr":
            j_ty.run_j(i)
        elif label[0] or label[1]  == "halt" or "noop":
            o_ty.run_o(i)
        else:
            break   
     
#j_ty.run_j("start  jalr  4  3")
runcode(open('test.txt'))

#run_itype("       lw 1 2 3")








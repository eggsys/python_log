import numpy as np
import time


COMMON_VAL = 5
list = [[1,2],[3,2],[9,1]]
len_list = len(list)
i = 0
kb_count = 0
_stop = False
print("####################")
while(kb_count < 10 and _stop == False):
    print("update : ",list)
    insert_val = input("insert value >> ")
    i = 0
    found = 0
    for x in list:
        print("<i count>")         
        print(i)
        if(i < len(list)):
            inside = list[i]        
            inside_p1 = inside[0]
            inside_p2 = inside[1]
            print("we are checking >", inside)        
            if( int(insert_val) == int(inside_p1) ):
                result = True

                print("position [",i,"] : count ++")
                print(inside_p2)
                inside_p2 = inside_p2 + 1
                list[i][1] = inside_p2
                found+=1

                if(inside_p2  == COMMON_VAL):
                    print("[DONE] we found the common number !")
                    _stop = True

            else:
                result = False
                print(result,"!!")
                found+=0          
        i+=1
        print("####################")

    if(found == 0 ):
        print("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
        print(insert_val,"is not found in",list)
        print("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
        list.append([insert_val,1])
        #print("is ",insert_val," inside :",list,"|----->",result)

            
    kb_count+=1
    print("-------------------------------------")


print("final data : ", list )
#print("####################")
#print("length : ",len(list))
#print("show inside list", list[0][0])
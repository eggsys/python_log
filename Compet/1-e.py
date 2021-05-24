def digital_root(n):

    arr = [int(d) for d in str(n)]

    if(len(arr)==1):
        return n
    else:
        while(len(arr)>1):
            temp = 0
            #print("len : ",len(arr))
        
            for x in arr:
                temp = temp+x
            arr = [int(d) for d in str(temp)]
            #print(temp)
        return temp

print(digital_root(132189))
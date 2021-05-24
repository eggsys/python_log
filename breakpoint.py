list = [1,2,3,4,5,6,7,8,9,10,11,11,1,2,3,5,6,9]
stop = False
for x in list: 
    while(not stop): 

        print(x)        
        if(x > 0):
            if(x>1):
                if(x>9):
                    #print(x)
                    stop = True
                    break


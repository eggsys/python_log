def descending_order(num):
    str1 = ""
    arr = [int(d) for d in str(num)]   
    result = sorted(arr,reverse=True)
    for ele in result: 
        str1 += str(ele)
        final = int(str1)

    return final


  
print(descending_order(123456789))
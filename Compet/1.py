def digital_root(n):
    arr = [int(d) for d in str(n)]
    temp = 0
    print("len : ",len(arr))
   
    for x in arr:
        temp = temp+x
    print(temp)

    arr = [int(d) for d in str(temp)]
    print("len : ",len(arr))
    temp = 0
    for x in arr:
        print(x)
        temp = temp+x
        print(temp)


digital_root(942)

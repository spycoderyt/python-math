def per(n,steps=0):
    digits = [int(i) for i in str(n)]

    result = 1
    for j in digits:
        result *= j
    print(result)
    steps += 1

    if len(str(result))==1:
        print("done")
        print("TOTAL STEPS:" + 
        str(steps))
    else:
        per(result,steps)    
        

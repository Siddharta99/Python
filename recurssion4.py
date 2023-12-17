#4
#4 * 3 *2*1
def Fact(No):
    #Ans = 1
    while(No <= 0):
        return 1
    else:
        return(No * Fact(No-1))

Ret = Fact(4)
       
print("Result is : ",Ret)
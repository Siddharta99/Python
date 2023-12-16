def checkeven(No):
    return (No % 2 == 0)

def square(No):
    return (No**2)

def filterX(Arr,Function_name):
    Result = []
    for no in Arr:
        if(Function_name(no)):
            Result.append(no)

    return Result
    
def mapX(Arr,Function_name):
    Result = []
    for no in Arr:
        value = Function_name(no)
        Result.append(value)
    return Result

def reduceX(Arr):
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    return Sum
def main():
    Data = [5,2,3,4,3,4,1,2,8,10]
    print("Original Data : ",Data)

    Data_Filter = list(filterX(Data,checkeven))
    print("Data after filter : ",Data_Filter)

    Data_map = list(mapX(Data_Filter,square))
    print("Data after Data_map : ",Data_map)

    Data_reduce = reduceX(Data_map)
    print("Data after reduce : ",Data_reduce)

if __name__ == "__main__":
    main()
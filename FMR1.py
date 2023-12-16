
def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+2

def filterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        Value = Function_Name(no)
        Result.append(Value)
    return Result
def reducerX(Arr,Function_Name)
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    return Sum
def main():
    Data = [2,3,1,6,4,5]

    Data_Filter = list(filterX(Data,CheckEven))
    print("Data after filter : ",Data_Filter)
    print("Data after mapX : ",Data_map)

if __name__ == "__main__":
    main()
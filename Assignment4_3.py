
def numbers(No):
    return (No>=70 and No<=90)

def Increment(No):
    return (No+10)
def filterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_name):
    Result = []
    for no in Arr:
        value = Function_name(no)
        Result.append(value)
    return Result

def reduceX(Arr):
    Product = 1
    for no in Arr:
        Product = Product * no
    return Product
def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Original Data : ",Data)

    Data_Filter = list(filterX(Data,numbers))
    print("Data after filter = ",Data_Filter)

    Data_map = list(mapX(Data_Filter,Increment))
    print("Data after map : ",Data_map)

    Ret = reduceX(Data_map)
    print("Data after reduce : ",Ret)
if __name__ == "__main__":
    main()
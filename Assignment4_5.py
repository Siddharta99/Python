def prime(No):
    n = print(int(input("Enter numbers : ")))
    for i in range(2,n):
        if n%i == 0:
            break
    if x+1 == n:
        print(n)

def filterX(Arr,Function_name):
    Result = []
    for no in Arr:
        if(Function_name(no)):
            Result.append(no)
    return Result

def main():
    Data = [2,70,11,10,17,23,31,77]
    print("Original Data : ",Data)

    Data_filter = list(filterX(Data,prime))
    print("Data after filter : ",Data_filter)
if __name__ == "__main__":
    main()
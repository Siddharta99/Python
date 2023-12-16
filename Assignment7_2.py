import threading

def evenfactor(No):
    sum=0
    for i in range(1,No):
        if(i%2 == 0):
            print("Even numbers : ",i)
            sum = sum+i
    print("even",sum)

def Oddfactor(No):
    sum=0
    for i in range(1,No):
        if(i%2 != 0):
            print("Odd numbers : ",i)
            sum=sum+i
    print("Odd",sum)
def main():
    No = int(input("enter the number"))
    Thread1=threading.Thread(target=evenfactor,args=(No,))
    Thread2=threading.Thread(target=Oddfactor,args=(No,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()
    print("exit from main")

if __name__ == "__main__":
    main()
import threading

def evenlist(No):
    No = list(No)
    sum=0
    for i in range (len(No)):
        if(No[i]%2 == 0):
            sum=sum + No[i]
    print("Even  : ",sum)

def oddlist(No):
    No = list(No)
    sum=0
    for i in range (len(No)):
        if(No[i]%2 != 0):
            sum=sum + No[i]
    print("Odd  : ",sum)

def main():
    No = [int(x) for x in input("enter numbers from space separate").split()]
    thread1 = threading.Thread(target=evenlist,args=(No,))
    thread2 = threading.Thread(target=oddlist,args=(No,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
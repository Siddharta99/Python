import threading

def DisplayEven(No):
    for i in range(1,No,1):
        if(i%2 == 0):
            print("Even Numbers : ",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i%2 != 0):
            print("Odd Numbers : ",i)

def main():
    Number = 10

    Even=threading.Thread(target=DisplayEven,args=(Number,))
    Odd=threading.Thread(target=DisplayOdd,args=(Number,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()
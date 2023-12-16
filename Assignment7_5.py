import threading

def numbers():
    for i in range(51):
        print(i)

def reversenumbers():
    for i in range(51,-1,-1):
        print(i)




def main():
    thread1 = threading.Thread(target=numbers,args=())
    thread2 = threading.Thread(target=reversenumbers,args=())

    thread1.start()
    thread2.start()

if __name__ == "__main__":
    main()
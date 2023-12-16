def Displayfactors(No):
    i = 1
    print("factors are : ")
    while(i <= int(No/2)):
        if (No % i == 0):
            print(i)
        i = i + 1
        

def main():
    print("Enter number : ")
    No = int(input())
    Displayfactors(No)




if __name__ == "__main__":
        main()

    

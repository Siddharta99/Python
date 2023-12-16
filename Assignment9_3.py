import sys
import os

if len(sys.argv) < 2 :
    print("Give filename using command line ")
    exit()
 

def main():
    if os.path.exists(sys.argv[1]):
        print("file exist")
    else:
        print("file does not exist")

    with open(sys.argv[1]) as f:
        with open("Demo.txt","w") as f1:
            for line in f:
                f1.write(line)
    

if __name__ == "__main__":
    main()
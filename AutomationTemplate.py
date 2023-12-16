from sys import *
from os import *

def Script_Task(No):
    if(No%2 == 0):
        print("It is even numbers")
    else:
        print("It is odd numbers")

def main():
    print("_______________marvellous Infosystem Automations_____________________________")
    print("Automation script started with name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This script is used to perform ____________________")
        exit()

    elif((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ___ number of arguments as")
        print("First Argument as :____________________")
        print("Second Argument as :_____________")
        exit()

    else:
        Script_Task(int(argv[11]))

        

if __name__ == "__main__":
    main()
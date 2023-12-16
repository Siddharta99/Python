

function = lambda A,B : A * B

def main():
    value1 = int(input("Enter first number"))
    value2 = int(input("Enter second number"))
    ret = function(value1,value2)
    print(ret)

if __name__ == "__main__":
    main()
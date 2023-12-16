class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        print("Enter 1st number")
        self.value1=int(input())
        print("Enter 2nd number")
        self.value2=int(input())

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1 / self.value2

def main():
    obj1 = Arithmetic()
    obj2 = Arithmetic()

    obj1.Accept()
    print("Addition is :{0}\n Subtraction is :{1} \n Multiplication is :{2} \n Division is :{3}".format(obj1.Addition(),obj1.Subtraction(),obj1.Multiplication(),obj1.Division()))

    obj2.Accept()
    print("Addition is :{0}\n Subtraction is :{1} \n Multiplication is :{2} \n Division is :{3}".format(obj2.Addition(),obj2.Subtraction(),obj2.Multiplication(),obj2.Division()))

if __name__ == "__main__":
    main()
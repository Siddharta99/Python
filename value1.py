
class value:

    def __init__(self,Data):
        self.No = Data

    def sumfactors(self):
        sum = 0

        for i in range(1,self.No):
            if(self.No % i == 0):
                sum = sum + i

        return sum

    def checkperfect(self):
        Ans = self.sumfactors()

        if(self,No == Ans):
            return True
        else:
            return False
def main():
    print("Please enter number")
    A = int(input())

    obj = value(A)

    Ret = obj.checkperfect()
    if(Ret == True):
        print("{} is a perfect number".format(A))
    else:
        print("{} is not a perfect number".format(A))

if __name__ == "__main__":
    main()
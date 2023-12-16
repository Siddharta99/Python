
class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()

    def Accept(self):
        print("Enter how many elements you want : ")
        self.size = int(input())

        print("Please enter the elements")
        value = 0
        for i in range(0,self.size):
            value = int(input())
            self.Arr.append(value)

    def Display(self):
        print("Elements from list are : ")
        for i in range(0,self.size):
            print(self.Arr[i])
    
    def Summation(self):
        sum = 0
        for i in range(0,self.size):
            sum = sum + self.Arr[i]
       
        return sum

    def Average(self):
        sum = 0
        for i in range(0,self.size):
            sum = sum + self.Arr[i]

        return (sum/self.size)

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0,self.size):
            if(self,Arr[i] > Max):
                Max = self.Arr[i]

        return Max
def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Summation of all elements is : ",Output)

    Output = obj.Average()
    print("Average of all elements is : ",Output)

    Output = obj.Maximum()
    print("Largest element is : ",Output)
    
if __name__ == "__main__":
    main()
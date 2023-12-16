#write a program which contains one class named as BankAccount.BankAccount class contains two instance variables as Name and Amount
#That class contains one class variable as ROI which is initialise to 10.5.Inside init method initialise init method 
#initialise all name and amount variables by accepting the values from user .There are four instance methods inside class
#as Display(),Deposit(),withdraw(),CalculateInterest().
#Deposit() method will accept the amount from user and add that value in class instance variable Amount.
#withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance
#variable Amount.CalculateIntrest() method calculate the interest based on Amount by considering rate of intrest which is
#class variable as ROI.And Display() method will display value of all the instance variables as Name and Amount.
#After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print("name is :{0} \t amount is : {1}".format(self.Name,self.Amount))

    def Deposit(self,depo):
        self.Amount += depo

    def Withdraw(self,depo):
        self.Amount -= depo

    def CalculateIntrest(self,time):
        simple_intrest = (self.Amount * time * BankAccount.ROI)/100
        print("The simple intrest is ",simple_intrest)

def main():
    Obj1 = BankAccount("ABC",3000)
    Obj1.Display()
    Obj1.Deposit(3000)
    Obj1.Display()
    Obj1.Withdraw(2000)
    Obj1.Display()
    Obj1.CalculateIntrest(2)

    Obj1 = BankAccount("CBA",3110)
    Obj1.Display()
    Obj1.Deposit(5000)
    Obj1.Display()
    Obj1.Withdraw(2001)
    Obj1.Display()
    Obj1.CalculateIntrest(5)

if __name__ == "__main__":
    main()


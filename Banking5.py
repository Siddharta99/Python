#Instance variable : Name,Amount,Address,AccountNo
#Instance method : CreateAccount(),DisplayAccountInfo()
#


class Bank_Account:
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your initial amount : ")
        self.Amount = int(input())
        
        print("Enter your Address : ")
        self.Address = input()
        
        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("--------Your Account Information is as below--------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Name of Account Holder : ",self.Address)
        print("current Amount in account : ",self.Amount)


    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is : ",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Government of India You have to submoit below documents")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of aadhar card")
        print("3 : Photo of PAN card")

    def Deposit(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value
        
def main():
    print("------Banking Application--------")

    print("--------calling static method to display KYC info--------")
    Bank_Account.DisplayKYCInfo()
    
    print("------Accessing the instance variable from main-------")
    print("Name of bank : ",Bank_Account.Bank_Name)
    print("Rate of Intrest on Fixed deposit : ",Bank_Account.ROI_On_FD)

    print("----calling the class method to display Bank information of first account-------")
    Bank_Account.DisplayBankInformation()
    
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first account")
    User1.CreateAccount()

    print("Creating the second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit(500)
    User2.Deposit(1200)

    print("Amount of {} after deposit is {}: ",User1.Amount)
    print("Amount of {} after deposit is {} : ",User2.Amount)

    User1.Withdraw(200)
    User2.Withdraw(3000)

    print("Amount of {} after deposit is {}: ",User1.Amount)
    print("Amount of {} after deposit is {}: ",User2.Amount)
if __name__ == "__main__":
    main()
class circle:
    PI=3.14
    def __init__(self):
        self.r=0.0
        self.a=0.0
        self.c=0.0
    def Accept(self):
        print("enter value of radius")
        self.r=float(input())
    def CalculateArea(self):
        self.a=self.PI*self.r*2
    def Calculatecircumference(self):
        self.c=self.PI*self.r*2
    def Display(self):
        print("area is:{0} \n circumference is:{1}".format(self.a,self.c))

def main():
    obj1 = circle()
    obj2 = circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.Calculatecircumference()
    obj1.Display

    obj2.Accept()
    obj2.CalculateArea()
    obj2.Calculatecircumference()
    obj2.Display()

if __name__ == "__main__":
    main()
class Demo:
    
    def __init__(self,no1,no2):
        self.i = no1
        self.j = no2
    def Fun(self):
        print(self.i)
        print(self.j)

    def Gun(self):
        print(self.i)
        print(self.j)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()

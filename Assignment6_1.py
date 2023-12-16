#write a program which contains one class named as Bookstore.Bookstore class contains two instance variables as Name,Author
#that class contains one class variable as NoOfbooks which initializes to 0.There is one instance methods of class as
#Display which displays name,Author and number of books.Initialise instance variable in init method by accepting the values from
#user as name and author .Inside init method increment value of NoOfBooks by one.
#After creating the class create the two objects of BookStore class as
#Obj1 = BookStore("Linux System Programming","Robert Love")
#Obj.Display()       #Linux System Programming by Robert Love.No of books : 1
#Obj2 = BookStore("C Programming","Denis Ritchie")
#Obj2.Display()  # C Programming by Dennis Ritchie.No of books : 2


class BookStore:
    NoOfBooks = 0
    def __init__(self,name,author):
        self.name=name
        self.author=author
        BookStore.NoOfBooks+=1

    def Display(self):
        print("book is:{0} \n author is:{1} \n no of books:{2}".format(self.name,self.author,self.NoOfBooks))

def main():
    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()  #Linux System Programming by Robert Love.No of books : 1
    
    Obj2 = BookStore("C Programming","Denis Ritchie")
    Obj2.Display()  #C Programming by Dennis Ritchie.No of books : 2

if __name__ == "__main__":
    main()

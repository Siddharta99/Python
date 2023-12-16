import os

def File(Name):
    if(os.path.isfile(Name)):
        print("File is already existing")
        return

    else:
        print("file is not existing")


def main():
    print("Enter the file that exists or not")
    Name = input()
    File(Name)


if __name__ == "__main__":
    main()
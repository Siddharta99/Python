from sklearn import tree

#Rough 1
#smooth 0
#Tennis 1
#Cricket 2

def BallPredictor():
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[35,1]]
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features,Labels)

    ret = obj.predict([[weight,surface]])
    if ret == 1:
        print("Your object looks like a tennis ball")
    else:
        print("Your object looks like a Cricket ball")

def main():
    print("----------Ball Predictor case sudy-------")

    print("Please enter the weight of your object in grams")
    weight = int(input)
    print("Please enter the type of surface of your object(Rough/Smooth)")
    surface = input()
    
    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Invalid type of surface")
        exit()

    BallPredictor(weight,surface)

if __name__ == "__main__":
    main()
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

def MarvellousKNeighboursClassifier():

    def fit(self,trainingdata, trainingtarget):
        self.TrainingData = trainingdata
        self.TrainingTarget = trainingtarget

    def closest(self,row):
        mimimumdistance = euc()
        minimumindex = 0

        for i in range(1,len(self.TrainingData)):
            Distance = euc(row,self.TrainingData[i])
            if Distance < minimumdistance:
                minimumdistance = Distance
                minimumindex = 1


        return self.TrainingData[minimumindex]
    def predict(self,TestData):
        predictions = []
        for value in TestData:
            result = closest(value)
            predictions.append(result)

        return predictions

    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size = 0.5)

    Classifier = MarvellousKNeighboursClassifier()

    Classifier.fit(Data_train,Target_train)

    Predictions = Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    return Accuracy

def main():
    MarvellousKNeighboursClassifier()

    print("Accuracy of Iris dataset with KNN is ",Ret * 100)

if  __name__ == "__main__":
    main()
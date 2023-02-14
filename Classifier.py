import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import numpy

class ClassifierA:
    def __init__(self, dataset):
        self.classifier = DecisionTreeRegressor(
            criterion="squared_error", splitter='random', random_state=3,
            max_depth=4, max_features='sqrt', min_samples_split=4
        )
        Xtrain, Ytrain = self.setTraining(self.importDataset(dataset))
        self.classifier.fit(Xtrain, Ytrain)

    def importDataset(self, dataset):
        balance_data = pd.read_csv(dataset, sep=',', header=None)
        return balance_data

    def setTraining(self, balanceData):
        X = balanceData.values[:, 0:6]
        Y = balanceData.values[:, 6]
        Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.000001, random_state=0)
        return Xtrain, Ytrain

    def classify(self, userInput):
        prediction = int(self.classifier.predict(userInput))
        if prediction == 1:
            return "your degree of emergency is: red"
        elif prediction == 2:
            return "your degree of emergency is: orange"
        elif prediction == 3:
            return "your degree of emergency is: yellow"


    def cross_validation(self):
        data = self.importDataset("DataSet.csv")
        X = data.values[:, 0:6]
        Y = data.values[:, 6]

        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.000001, random_state=0)

        clf = DecisionTreeRegressor(
            criterion="squared_error",splitter='random', random_state=3,
            max_depth=4, max_features='sqrt', min_samples_split=5)

        score = cross_val_score(clf, X_train, y_train, cv=4)
        accurancy = numpy.round(score.mean(), 2)
        deviation = numpy.round(score.std(), 2)
        return("Risultati cross validation:\nAccurancy: " + str(accurancy) + "\nDeviation: " + str(deviation))

    def metrix_test(self):
        data = self.importDataset("DataSet.csv")
        X = data.values[:, 0:6]
        Y = data.values[:, 6]

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

        clf = DecisionTreeRegressor(
            criterion="squared_error",splitter='random', random_state=3,
            max_depth=4, max_features='sqrt', min_samples_split=14)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test, clf)

        mean = numpy.round(mean_squared_error(y_test, y_pred), 2)
        score = numpy.round(r2_score(y_test, y_pred), 2)
        metricsTestsResults = ("Risultati delle metriche:\nMean squared error: " + str(mean) + "\nr-quadro score: " + str(score))
        return metricsTestsResults










from sklearn import linear_model
from sklearn.model_selection import KFold, cross_validate
import pandas as pd
import numpy as np
import pickle

def makeTestData():
    data  = [
        [0.7, 4, 15, 9, 9, 10],
        [0.8, 4, 14, 8, 9, 9],
        [0.8, 4, 12, 8, 9, 9],
        [0.6, 3, 13, 9, 10, 9],
        [0.7, 4, 10, 7, 10, 10],
        [0.7, 2, 8, 10, 10, 9],
        [0.8, 3, 15, 5, 5, 7],
        [0.5, 3, 7, 5, 5, 5]
    ]

    data = pd.DataFrame(data=data)
    jsonData = data.to_json()

    return jsonData


class estimator:
    def __init__(self):
        self.clf = self.loadModel()

    def loadModel(self):
        fileName = "../model/model.pkl"
        clf = pickle.load(open(fileName, 'rb'))
        return clf

    def makeTestData(self,rowData):
        makeTestData = pd.read_json(rowData)
        return makeTestData

    def execPredict(self, testData):
        score = self.clf.predict(testData)
        print(score)
        result = pd.DataFrame(data=score,columns=['data'])

        resJ = result.to_json()

        return resJ
import json
import pandas as pd
from pandas.io.json import json_normalize

class DataSetOp():
    def obtenerDataFrame(self, jsonData):
        matrix = []
        columns = []
        for result in jsonData:
            for index in result.keys():
                columns = list(result[index])
                vector = []
                for value in result[index].keys():
                    vector.append(result[index][value])
            matrix.append(vector)
        return pd.DataFrame(matrix, columns=columns)
    
    def obtenerJsonArchivo(self, dirArchivo):
        #funciona únicamente con el JSON para estructura del dataset del clima
        with open(dirArchivo) as json_file:
            data = json.load(json_file)
            return data['results']

dataSet = DataSetOp()

dirArchivo = 'data.json'

results = dataSet.obtenerJsonArchivo(dirArchivo)

dataFrame = dataSet.obtenerDataFrame(results)

print(dataFrame)
import input
import cosin
import csv
import numpy as np

def predict():

    test = []
    
    with open('dataInput.csv', 'r') as csv_file:
        input = csv.reader(csv_file)
        for row in input:
            test.append(row)
        # print(test[0])

    with open('data.csv', 'r') as csv_file:
        train = csv.reader(csv_file)
        for row in train:
            

predict()
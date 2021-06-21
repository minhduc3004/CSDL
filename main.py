from math import dist
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

    train = []

    with open('data.csv', 'r') as csv_file:
        file = csv.reader(csv_file)
        for row in file:
            train.append(row)

    tmp = 0
    distance = 1000
    cur_label = 0
    arr_distance = []
    while tmp<113:
        for i in range(181):
            minh=int(train[tmp*181+i][4])
            if(minh==cur_label):
                train[tmp*181+i].pop(4)
                cosin_similarity = cosin.cosin_distance(test[i],train[tmp*181+i])
                print(cosin_similarity)
                if distance > cosin_similarity and cosin_similarity>0:
                    distance = cosin_similarity
            else:
                arr_distance.append(distance)
                cur_label += 1
                distance = 1000
        tmp += 1

    res_label = -1
    min_distance = 100
    print(arr_distance)
    for i in range(np.shape(arr_distance)[0]):
        if min_distance > arr_distance[i]:
            min_distance = arr_distance[i]
            res_label = i
    print(res_label)

predict()
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
        # print(train[400][3])
        print(np.shape(train)[0])

    tmp = 1
    distance = 1000000000
    cur_label = 0
    arr_distance = []
    # print(np.shape(train)[0]/np.shape(test)[0])
    # print(train[0])
    train[0].remove[4]
    print(train[0])
    # print(cosin.cosin_distance(test[100],train[100].pop[4]))
    # while tmp < (np.shape(train)[0]/np.shape(test)[0]):

    #     for i in range(np.shape(test)[0]):
    #         if(train[tmp+i][4]==cur_label):
    #             train[tmp+i].pop[4]
    #             cosin_similarity = cosin.cosin_distance(test[i],train[tmp+i])
    #             if distance > cosin_similarity:
    #                 distance = cosin_similarity
    #         else:
    #             arr_distance.append(distance)
    #             cur_label += 1
    #     tmp += 1

    # res_label = -1
    # min_distance = 1000000000
    # print(arr_distance)
    # print(np.shape(arr_distance)[0])
    # for i in range(np.shape(arr_distance)[0]):
    #     if min_distance > arr_distance[i]:
    #         min_distancen = arr_distance[i]
    #         res_label = i
    # print(res_label)

predict()
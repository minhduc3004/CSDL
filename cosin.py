from typing import Sized
import numpy as np
import math

def tich_vo_huong(a,b):
    sum = 0;
    for i in range(a.size):
        sum += a[i]*b[i]

def do_dai_vector(a): 
    tong = np.array([sum(a**2)])
    res = math.sqrt(tong[0])
    return res

def cosin_distance(a,b):
    return tich_vo_huong(a,b) / (do_dai_vector(a)*do_dai_vector(b))

# a = [1,2,3]
# print(do_dai_vector(np.array(a)))
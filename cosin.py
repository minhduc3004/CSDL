from typing import Sized
import numpy as np
import math

def tich_vo_huong(a,b):
    sum = 0
    for i in range(np.shape(a)[0]):
        sum += float(a[i])*float(b[i])
    return sum

def do_dai_vector(a): 
    sum=0
    for i in a:
        sum+=float(i)**2
    res=math.sqrt(sum)
    if res==0:
        return 0.0000001
    return res

def cosin_distance(a,b):
    return tich_vo_huong(a,b) / (do_dai_vector(a)*do_dai_vector(b))

# a = [1,2,3]
# print(do_dai_vector(np.array(a)))
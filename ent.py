#coding: utf-8

__author__ = 'bozyao'

from math import log
from numpy import array

def getEnt(dict):
    '''
    给入字典统计结果，给出此结果的熵
    
    dict：  统计的数据结果
    返回：  香农熵
    '''
    ent = 0.0
    total = array(dict.values()).sum()
    for key in dict:
        proportion = dict[key] * 1.0 / total
        ent -= proportion * log(proportion, 2)
    return ent

if __name__ == '__main__':
    dict = {}
    for i in range(100):
        if i % 3 == 0:
            dict[3] = dict.get(3, 0) + 1
        elif i % 2 == 0:
            dict[2] = dict.get(2, 0) + 1
        else:
            dict[1] = dict.get(1, 0) + 1
    print dict
    print getEnt(dict)

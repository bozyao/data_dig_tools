#coding:utf-8
__author__ = 'bozyao'

from numpy import *

def norm(dataSet):
    '''
    对多维数组进行归一化操作

    dataSet：   多维数组
    返回：      归一化后的数组，差值列表，最小值列表 
    '''
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1)) 
    normDataSet = normDataSet/tile(ranges, (m,1)) 
    return normDataSet, ranges, minVals

if __name__ == '__main__':
    dataSet = random.rand(4,4)
    print dataSet
    print norm(dataSet)

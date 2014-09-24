#coding: utf-8
__author__ = 'bozyao'

from numpy import *

def getMinDis(data, dataSet, n): 
    ''' 
    data:   准备计算记录的数据，格式为一个数组，如：[3, 7.0, 8]
    dataSet:进行对比的数据集合，一个二维数据
    n:      返回最接近的几条数据？
    返回：  排序的，由大到小的，距离数据及数据数组，数组长度小于等于n
    '''
    dataSetSize = dataSet.shape[0]
    diffMat = tile(data, (dataSetSize,1)) - dataSet
    sqDiss = (diffMat**2).sum(axis=1)
    diss = sqDiss ** 0.5 
    sort = diss.argsort() 
    retDiss = []
    retData = []
    for i in range(n):
        retDiss.append(diss[sort[i]])
        retData.append(dataSet[sort[i]])
    return retDiss, retData

if __name__ == '__main__':
    #dataSet = random.rand(4,4)
    dataSet = array([[ 0.51256002,  0.95027049,  0.40472456,  0.66041653],
                [ 0.87677254,  0.57921246,  0.50303306,  0.1168142 ],
                [ 0.17554148,  0.34825289,  0.72334947,  0.96223441],
                [ 0.45509905,  0.77114424,  0.60491319,  0.95815854]])
    print getMinDis([0.4, 0.6, 0.5, 0.2], dataSet, 1)	

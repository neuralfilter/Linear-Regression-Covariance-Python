import sys
import pandas as pd
import numpy as np

print "file name: \n"

input_swag = raw_input()
data = pd.read_csv(input_swag) #read data in non-transposed  

print "file predictor: \n"

TypePredictor = (raw_input("enter the column name for predictor value \n"))
y_column = data[TypePredictor]
y_column_cov = y_column.T
y_column_cov = list(y_column_cov)
y_column_cov = pd.Series(y_column_cov)

data = data.drop(TypePredictor,1) #drop columns for data
t_data = data.T


length_of_data = len(data.columns)
print "number of M's"

MsInput = int(raw_input())

if length_of_data % MsInput  ==  0: #divisible?
    print "The number of M's works!"
elif length_of_data / MsInput == length_of_data:
    print "The Number of M's works!"
else:
    print "cannot divide this number"
    sys.exit() #exit system

"""
IMPROVED VERSION: 
-REQUIRES USE OF MULTI-INDEX INSTEAD OF STATIC METHOD: U WOT M8
-POSSIBLE IMPLEMENTATION OF COMPOSED ARRAYS
-CHANGE IF STATEMENTS TO WHILE/FOR
"""

maxIndexes = len(t_data.index) #number of data
temporary_data = data # store data to delete and check 
clustersize = maxIndexes / MsInput #size of one cluster
print clustersize

def finalcluster1 ():
    global group_rows1
    group_rows1_swag = np.random.choice(t_data.index.values, int(clustersize), replace=False)
    group_rows1 = group_rows1_swag.tolist()
    final_cluster1 = data[group_rows1]
    return final_cluster1

def finalcluster2 ():
    global group_rows2
    group_rows2_swag = np.random.choice(t_data.index.values, int(clustersize), replace=False)
    group_rows2 = group_rows2_swag.tolist()
    final_cluster2 = data[group_rows2]
    return final_cluster2

def finalcluster3 ():
    global group_rows3
    group_rows3_swag = np.random.choice(t_data.index.values, int(clustersize), replace=False)
    group_rows3 = group_rows3_swag.tolist()
    final_cluster3 = data[group_rows3]
    return final_cluster3

def finalcluster4 ():
    global group_rows4
    group_rows4_swag = np.random.choice(t_data.index.values, int(clustersize), replace=False)
    group_rows4 = group_rows4_swag.tolist()
    final_cluster4 = data[group_rows4]
    return final_cluster4

if MsInput == 1:
    clusters1 = finalcluster1()
    print "clustering has finished"
elif MsInput == 2:
    clusters1 = finalcluster1()
    clusters2 = finalcluster2()
    print "clustering has finished"
elif MsInput == 3:
    clusters1 = finalcluster1()
    clusters2 = finalcluster2()
    clusters3 = finalcluster3()
    print "clustering has finished"
elif MsInput == 4:
    clusters1 = finalcluster1()
    clusters2 = finalcluster2()
    clusters3 = finalcluster3()
    clusters4 = finalcluster4()
    print "clustering has finished"
    
covariance = []
covariance2 = []
covariance3 = []
covariance4 = []

def c_covariance(x):
    x = x.T
    x = list(x)
    x = pd.Series(x)
    x = y_column_cov.cov(x)
    x = str(x)
    x = float(x)
    covariance.append(x)
    
def c_covariance2(x):
    x = x.T
    x = list(x)
    x = pd.Series(x)
    x = y_column_cov.cov(x)
    x = str(x)
    x = float(x)
    covariance2.append(x)

def c_covariance3(x):
    x = x.T
    x = list(x)
    x = pd.Series(x)
    x = y_column_cov.cov(x)
    x = str(x)
    x = float(x)
    covariance3.append(x)

def c_covariance4(x):
    x = x.T
    x = list(x)
    x = pd.Series(x)
    x = y_column_cov.cov(x)
    x = str(x)
    x = float(x)
    covariance4.append(x)


if MsInput == 1:
    print clusters1
    clusters1.apply(c_covariance, axis=0)
elif MsInput == 2:
    print clusters1
    clusters1.apply(c_covariance, axis=0)
    print clusters2
    clusters2.apply(c_covariance2, axis=0)
elif MsInput == 3:
    print clusters1
    clusters1.apply(c_covariance, axis=0)
    print clusters2
    clusters2.apply(c_covariance2, axis=0)
    print clusters3
    clusters3.apply(c_covariance3, axis=0)
elif MsInput == 4:
    print clusters1
    clusters1.apply(c_covariance, axis=0)
    print clusters2
    clusters2.apply(c_covariance2, axis=0)
    print clusters3
    clusters3.apply(c_covariance3, axis=0)
    print clusters4
    clusters4.apply(c_covariance4, axis=0)
    
print covariance
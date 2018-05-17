##knn implementation


import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

dataset=pd.read_csv('Video Features.csv',encoding = "ISO-8859-1")

#knn handel bad for outliers if we don't remove id col.

dataset.drop(['Song','Song Id'],1,inplace=True)

x=np.array(dataset.drop(['class'],1))
y=np.array(dataset['class'])


#test=pd.read_csv('test.csv')

#knn handel bad for outliers if we don't remove id col.

# test.drop(['id','name'],1,inplace=True)


# x_test=np.array(test.drop(['class'],1))
# y_test=np.array(test['class'])


x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.4)


#classifier
clf=neighbors.KNeighborsClassifier()
clf.fit(x_train,y_train)

#accuracy measure
accuracy=clf.score(x_test,y_test)
print('video analysis accuracy using knn is:')
print(accuracy)



# example_measure=np.array([7.782763354,2903.467941,21.66916186,6330.903385,2788.875991,89.10290948,9.171683311])
# example_measure=example_measure.reshape(1,-1)

# prediction=clf.predict(example_measure)
# print(prediction)
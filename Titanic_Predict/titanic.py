import pandas
tit = pandas.read_csv("train.csv")

#print tit.describe()


tit["Age"] = tit["Age"].fillna(tit["Age"].median())
print tit.describe()

print tit["Sex"].unique()
tit.loc[tit["Sex"]=="male","Sex"] = 0
tit.loc[tit["Sex"]=="female","Sex"] = 1

print tit["Embarked"].unique()
tit["Embarked"] = tit["Embarked"].fillna('S')

tit.loc[tit["Embarked"]=="S","Embarked"] = 0
tit.loc[tit["Embarked"]=="C","Embarked"] = 1
tit.loc[tit["Embarked"]=="Q","Embarked"] = 2

from sklearn.linear_model import LinearRegression

from sklearn.cross_validation import KFold


predictors = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
alg = LinearRegression()
kf = KFold(tit.shape[0],n_folds=3,random_state=1)

predictions = []
for train,test in kf:

    train_predictors = tit[predictors].iloc[train,:]
    train_target = tit["Survived"].iloc[train]
    alg.fit(train_predictors,train_target)
    test_predictors = alg.predict(tit[predictors].iloc[test,:])
    predictions.append(test_predictors)

import numpy as np

predictions = np.concatenate(predictions,axis=0)

predictions[predictions>.5] = 1
predictions[predictions<=.5]= 0
accuracy = sum(predictions[predictions == tit["Survived"]])/len(predictions)

print accuracy


from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression

alg = LogisticRegression(random_state=1)
scores = cross_validation.cross_val_score(alg,tit[predictors],tit["Survived"],cv=3)
print (scores.mean())


from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier


predictors = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
alg = RandomForestClassifier(random_state=1,n_estimators=10,min_samples_split=2,min_samples_leaf=1)
kf = cross_validation.KFold(tit.shape[0],n_folds=3,random_state=1)
scores = cross_validation.cross_val_score(alg,tit[predictors],tit["Survived"],cv=kf)
print (scores.mean())



alg = RandomForestClassifier(random_state=1,n_estimators=50,min_samples_split=4,min_samples_leaf=2)
kf = cross_validation.KFold(tit.shape[0],n_folds=3,random_state=1)
scores = cross_validation.cross_val_score(alg,tit[predictors],tit["Survived"],cv=kf)
print (scores.mean())

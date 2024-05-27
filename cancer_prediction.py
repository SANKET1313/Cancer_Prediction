# -*- coding: utf-8 -*-
"""Cancer Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zx168mhlcjAMXSy_xwRMLxdiQhjRZiNp
"""

!pip install pandas-profiling
from ydata_profiling import ProfileReport

import pandas as pd

cancer = pd.read_csv('/content/Cancer Prediction/Cancer.csv')

cancer.head()

cancer.info()

cancer.info()

cancer = pd.read_csv("/content/Cancer Prediction/Cancer.csv")
profile= ProfileReport(cancer,title="Cancer Prediction")
profile.to_notebook_iframe()
profile.to_file("Cancer Report.html")

cancer.columns

y = cancer['diagnosis']

X = cancer.drop(['id','diagnosis','Unnamed: 32'],axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=5000)

model.fit(X_train,y_train)

model.intercept_

model.coef_

y_pred = model.predict(X_test)

y_pred

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

confusion_matrix(y_test,y_pred)

accuracy_score(y_test,y_pred)

print(classification_report(y_test,y_pred))
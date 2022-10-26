import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

data = pd.read_csv("Pgv.csv")
data.head(3)

column_sels=['Mw','Distance','Depth']
X=data.loc[:,column_sels]
y=data['logpgv']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size = 0.2, random_state = 4)

print(X_train.shape,
X_test.shape,
y_train.shape,
y_test.shape)

from xgboost import XGBRegressor

reg = XGBRegressor()

reg.fit(X_train, y_train)
reg.save_model('model.json')

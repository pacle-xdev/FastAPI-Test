from sklearn.linear_model import LinearRegression
import numpy as np

data=[[0,11], [1,12.21], [2,13.42], [3,12.74], [4,15.64], [5,18.43], [6,20.43], [7,18.3]]
X = np.array(data)[:,0].reshape(-1,1)
y = np.array(data)[:,1].reshape(-1,1)

to_predict_x= [171,172,173,174,175,176,177,178,179,180,181,181,182,183,184,185,186,187,188,189,190,191,192,193,194,
               195,196,197,198,199,200]
to_predict_x= np.array(to_predict_x).reshape(-1,1)

reg=LinearRegression()
reg.fit(X,y)
predicted_y= reg.predict(to_predict_x)
print("Predicted y:\n",predicted_y)

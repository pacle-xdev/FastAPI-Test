import matplotlib.pyplot as plt
import random
randomlist = []
for i in range(0,200):
	n = random.randint(1,30)
	randomlist.append(n)

######## Using third party libray.########

import pandas as pd
df = pd.DataFrame (randomlist, columns = ['number'])
print (df.number[:170])

from statsmodels.tsa.statespace.sarimax import SARIMAX
ARMAmodel = SARIMAX(df.number[170], order = (1, 0, 1))
ARMAmodel = ARMAmodel.fit()

pred = ARMAmodel.get_forecast(len(df.index))
pred_df = pred.conf_int(alpha = 0.05)

pred_df["Predictions"] = ARMAmodel.predict(start = pred_df.index[170], end = pred_df.index[-1])
pred_df.index = df.index
pred_out = pred_df["Predictions"]

print(pred_out)

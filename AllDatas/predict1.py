import pandas as pd
df = pd.DataFrame (randomlist, columns = ['number'])
print (df)
​
from statsmodels.tsa.statespace.sarimax import SARIMAX
ARMAmodel = SARIMAX(df.number, order = (1, 0, 1))
ARMAmodel = ARMAmodel.fit()
​
pred = ARMAmodel.get_forecast(len(df.index))
pred_df = pred.conf_int(alpha = 0.05)
​
pred_df.loc["Predictions"] = ARMAmodel.predict(start = pred_df.index[0], end = pred_df.index[-1])
pred_df.index = df.index
pred_out = pred_df["Predictions"]
​
print(pred_out)


from datetime import datetime
def to_timestamp(dateString):
    element = datetime.strptime(dateString, '%m/%d/%Y')
    return int(datetime.timestamp(element))
# Will be used later to convert back
def to_date(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime('%m/%d/%Y')
start_ts = to_timestamp(START_DATE)
end_ts = to_timestamp(END_DATE)
from fastapi import FastAPI, Path
from typing import Optional
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.linear_model import LinearRegression
import requests
import json
import time
import asyncio
import websockets
#Haha
app = FastAPI()

# dataList =     [ 1210.7490548626397, 1210.1865426255044, 1207.5246845531901, 1208.667487534985, 1207.960768017857, 1207.5599512021222, 1208.154259303905, 1208.9932853878317, 1208.685840578701, 1208.5854078198454, 1209.1667348397173, 1209.2356628143832, 1208.9059789136438, 1207.1191143058845, 1207.6071024095622, 1207.081659772625, 1207.2414612457355, 1208.749989184566, 1209.9744347388125, 1209.8809903757647, 1210.844549991074, 1210.9734297856971, 1211.071299331642, 1210.800839450282, 1210.4440696760544, 1209.454298785134, 1210.5324528231636, 1210.687368773668, 1210.5169216489198, 1210.1831921121993, 1209.2621651368856, 1209.3199760129953, 1209.1304405492676, 1211.0852515744448, 1210.809005741712, 1210.7072930034121, 1209.9190852750542, 1210.578624761958, 1211.0064391663134, 1211.1914111396347, 1210.1391006220153, 1209.8364755398372, 1210.0230783341879, 1210.4432652237483, 1208.7677648739345, 1208.9311437038027, 1208.848127807064, 1209.4604797111622, 1211.0640399167687, 1211.7996435036287, 1213.3644618133233, 1212.1897826410357, 1212.6238413796057, 1213.323693843554, 1213.9080819777141, 1213.6146868918925, 1213.1819711129378, 1214.0205622341634, 1214.2495401646784, 1214.2788527576934, 1214.5354444096008, 1215.293598533062, 1213.2522547800556, 1213.8523354644542, 1214.3807592027947, 1217.8050555403242, 1217.3671219865525, 1215.1907358600345, 1214.6070816287363, 1214.5743256507783, 1213.8307594893288, 1213.3512274878228, 1213.9441281722295, 1213.680292174216, 1213.144381285554, 1212.5865628452339, 1212.4444031089063, 1213.691921428501, 1213.0111612940345, 1212.436927847358, 1211.540234549542, 1211.160689742009, 1210.9762874572568, 1210.870775945124, 1211.07688379741, 1210.7333551402685, 1210.2465890026356, 1213.5085968283438, 1213.1030461090945, 1212.9097957397682, 1210.6296489610356, 1209.718254157859, 1218.6190393880374, 1222.016121895971, 1218.8384414049247, 1216.7997690186617, 1216.5372762678444, 1218.7691895361625, 1220.4267862270028, 1223.5602923522486, 1225.0109453619564, 1223.4134578525225, 1220.7738804397106, 1220.0814053385184, 1219.4333367258498, 1218.7426867748031, 1217.5464487738411, 1216.9825949547555, 1209.558435687758, 1208.6410081457802, 1210.334516063067, 1207.8492269699111, 1209.0893294771931, 1209.844788118162, 1210.203293532714, 1211.4546946523228, 1213.8457068023788, 1213.9280516621136, 1212.4923594859813, 1212.9758729466632, 1212.2366444922811, 1212.7579867406228, 1214.0713595276577, 1213.3960131497856, 1212.5199150857802, 1212.949932905404, 1212.3494894147734, 1212.2117331384572, 1211.959974644434, 1212.265959044375, 1212.3348317111413, 1211.3276543735878, 1212.219113921696, 1211.5356027496873, 1213.8224270440369, 1216.2827432292415, 1217.2211680425012, 1216.2555557207145, 1214.874147188919, 1216.1538034138405, 1215.8692449153575, 1216.6275356861586, 1217.437088240886, 1217.227251459218, 1215.9622457287105, 1215.686392937237, 1217.756680736865, 1218.110665741132, 1216.9492117030202, 1217.8708326052006, 1217.5723796999766, 1216.2783191025394, 1216.9141254235562, 1216.36315243224, 1216.71507361041, 1216.9350459744985, 1218.7705128449163, 1219.3280440105605, 1219.990031461977, 1220.4794027846187, 1218.7819812208666, 1218.2774793161993, 1217.5257951093317, 1216.921212464401, 1212.1638078412561, 1213.2804360833359, 1213.8900609375348, 1213.181209631536, 1213.4266015827795, 1213.804933850983, 1213.3695611999246, 1213.7405837988083, 1214.796851432211, 1214.3547657230567, 1215.2717588138996, 1215.7901784812238, 1216.2002872896066, 1215.6366916203733, 1214.8684162671886, 1217.0342882691373, 1217.0243391511467, 1216.1260742739657, 1215.8011959293403, 1216.5115664242726, 1216.3965968738842, 1214.655674573518, 1215.678537684912, 1217.368614413909, 1216.9712883145846, 1219.0266528740005, 1218.2922789843358, 1217.6909367903625, 1217.7850477997042, 1219.5403264179754, 1220.4810046732928, 1221.3186274827722, 1218.3340564095765, 1218.2189267800018, 1218.0525999922716, 1217.8888916641765, 1218.6206878905346, 1218.5017008829277, 1219.5622488623633, 1217.5321569397456, 1216.049094193093, 1214.71447918689, 1214.730794646804, 1215.5835166543334, 1215.4541596506085, 1213.9005627541678, 1212.6233447144532, 1207.7130415023162, 1209.3652196942742, 1209.095577212315, 1209.8605207072858, 1211.944546061773, 1213.0997013608337, 1211.4934764723496, 1211.2257473328718, 1210.3375504087815, 1211.4121361904408, 1211.8545384128047, 1211.7704208662474, 1212.2075182289348, 1212.8628507659487, 1212.735956404837, 1211.8724203069085, 1212.0517751247914, 1212.3063632866138, 1210.8191126300417, 1211.984092793918, 1210.9509789159647, 1211.8476323002667, 1212.1307532527405, 1211.4059057457025, 1210.9239041173669, 1211.4691653976056, 1210.637262426086, 1209.7545898827905, 1208.9800902402292, 1209.585480546617, 1210.4349006701598, 1209.4536354892846, 1209.4803773440524, 1211.2583783184962, 1210.6870081073148, 1211.200653280237, 1210.951301097581, 1211.362518757394, 1210.4365167945225, 1210.1678040264485, 1209.985707092456, 1209.4999344887685, 1209.4173143059784, 1208.0628586764553, 1208.9850850079329, 1209.4160802214808, 1208.0107539038881, 1208.9494164883238, 1209.213959187607, 1207.968830475182, 1207.061699878708, 1207.4587558190035, 1208.2782098662897, 1208.7987849876802, 1208.624470706044, 1209.5966661495584, 1210.0966147682593, 1210.9807358288228, 1211.0252239524345, 1211.0713717636422, 1211.1116732404207, 1211.3697912904324, 1211.7387693914739, 1211.25991735652, 1211.4767787732796, 1212.2758222413188, 1212.6804253750709, 1213.352276530878, 1212.5074517360745, 1213.0746718763883, 1212.300181480306, 1212.4728013291242, 1212.439657345155, 1212.5270220875432, 1212.4057457252854, 1213.9514882345634, 1213.7992825919578, 1213.681550973718]
dataList = []

@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/price-prediction")
def price_prediction():
  df = pd.DataFrame(dataList, columns=['data'])
  print(df)

  ARMAModel = SARIMAX(df.data, order = (1, 0, 1))
  ARMAModel = ARMAModel.fit()

  pred = ARMAModel.get_forecast(len(df.index))
  pred_df = pred.conf_int(alpha = 0.05)

  print(pred_df.index[0],  pred_df.index[-1])
  pred_df["Predictions"] = ARMAModel.predict(start = pred_df.index[0], end = pred_df.index[-1])
  pred_df.index = df.index
  pred_out = pred_df["Predictions"]
  print(pred_out)
  return {"Data": pred_out}

async def getPrice():
  async with websockets.connect("wss://stream.binance.com:9443/ws/ETHUSDT@kline_1m") as websocket:
    await websocket.recv("message")

async def handler(websocket: WebSocketClientProtocol) -> None:
  async for message in websocket:
    print(message)

async def listenMsg() -> None:
  websocket_url = f"wss://stream.binance.com:9443/ws/ETHUSDT@kline_1m"
  async with websockets.connect(websocket_url) as websocket:
    await handler(websocket)

loop = asyncio.get_event_loop()
loop.run_until_complete()
asyncio.run(getPrice())

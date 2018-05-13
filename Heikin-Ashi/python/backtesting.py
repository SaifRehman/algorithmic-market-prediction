# Backtesting for a certain date
import requests
import json
def heikenashi_calc (date,startTime,endTime,flag,Prev_HA_Open,Prev_HA_Close):
    if(flag == 0):
        response = requests.get('https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate='+date+'&StartTime='+startTime+'&EndTime='+endTime+'&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C')
        if(response.status_code == 200):
            latest = response.content
            latest = json.loads(latest)
            latest = latest[0]
            if(latest["Open"]!=0 and latest["Close"]!=0 and latest["Low"]!=0 and latest["High"]!=0 ):
                HA_Open_latest = (Prev_HA_Open+Prev_HA_Close) /2
                HA_Close_latest = (latest["Open"] + latest["Close"] +  latest["Low"] + latest["High"]) /4
                return HA_Open_latest,HA_Close_latest
        # do something
    else:
        #do someting
        response = requests.get('https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate='+date+'&StartTime='+startTime+'&EndTime='+endTime+'&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C')
        if(response.status_code == 200):
            latest = response.content
            latest = json.loads(latest)
            latest = latest[0]
            if(latest["Open"]!=0 and latest["Close"]!=0 and latest["Low"]!=0 and latest["High"]!=0 ):
                HA_Open_latest = (Prev_HA_Close+Prev_HA_Open) /2
                HA_Close_latest = (latest["Open"] + latest["Close"] +  latest["Low"] + latest["High"]) /4
                return HA_Open_latest,HA_Close_latest

def heikenashi_predict(HA_Open_Current,HA_Close_Prev):
    if(HA_Open_Current<HA_Close_Prev):
        return True
    else:
        return False

Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","00:00","02:00",0,1313.60,1315.33))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","02:00","04:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","04:00","06:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","06:00","08:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","08:00","10:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","10:00","12:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","12:00","14:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","14:00","16:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","16:00","18:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","18:00","20:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","20:00","22:00",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)
Prev_HA_Open, Prev_HA_Close = (heikenashi_calc("5/9/2018","22:00","23:59",1,Prev_HA_Open,Prev_HA_Close))
a = heikenashi_predict(Prev_HA_Open,Prev_HA_Close)
print (a,Prev_HA_Open,Prev_HA_Close)

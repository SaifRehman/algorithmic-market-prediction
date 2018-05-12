import requests
import json
response = requests.get("https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate=5/11/2018&StartTime=11:00&EndTime=13:00&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C")
if(response.status_code == 200):
    prev = response.content
    prev = json.loads(prev)
    prev = prev[0]
    print prev
response = requests.get("https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate=5/11/2018&StartTime=13:00&EndTime=15:00&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C")
if(response.status_code == 200):
    latest = response.content
    latest = json.loads(latest)
    latest = latest[0]
    print latest
HA_Close_Prev = (prev["Open"] + prev["Close"] +  prev["Low"] + prev["High"]) /4
HA_Open_Prev = (prev["Open"] + prev["Close"]) /2
HA_Open_latest = (HA_Close_Prev + HA_Open_Prev) /2
HA_Close_latest = (latest["Open"] + latest["Close"] +  latest["Low"] + latest["High"]) /4


print HA_Close_Prev
print HA_Open_Prev
print HA_Close_latest
print HA_Open_latest



if (HA_Open_latest < HA_Close_Prev):
    print "buy"
else:
    print "sell"
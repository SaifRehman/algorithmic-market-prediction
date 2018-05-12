import requests
import json
response = requests.get("https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate=5/11/2018&StartTime=05:00&EndTime=7:00&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C")
if(response.status_code == 200):
    latest = response.content
    latest = json.loads(latest)
    latest = latest[0]
    print latest
HA_Open_latest = (1320.978+1319.854) /2
HA_Close_latest = (latest["Open"] + latest["Close"] +  latest["Low"] + latest["High"]) /4

print HA_Close_latest
print HA_Open_latest



if (HA_Open_latest < HA_Close_latest):
    print "buy"
else:
    print "sell"
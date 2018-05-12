import requests
import json
from twilio.rest import Client
from datetime import datetime, timedelta
from flask import Flask, request
import schedule
import time
from threading import Thread
app = Flask(__name__)
global HA_Close_latest 
HA_Close_latest = 0 
global HA_Open_latest 
HA_Open_latest = 0
global temp
temp = 0
def sms():
    print("Running periodic task!")
    utc_datetime_current = datetime.datetime.utcnow()
    utc_datetime_prev = utc_datetime_current - timedelta(hours=2)
    utc_datetime_prev = utc_datetime_prev.strftime("%Y/%m/%d %H:%M")
    utc_datetime_current = utc_datetime_current.strftime("%Y/%m/%d %H:%M")
    split_utc_datetime_current = utc_datetime_current.strip(' ')
    date_utc_datetime_current = split_utc_datetime_current[0]
    time_utc_datetime_current = split_utc_datetime_current[1]
    split_datetime_prev = utc_datetime_prev.strip(' ')
    time_utc_datetime_prev = split_utc_datetime_prev[1]
    response = requests.get('https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate='+date_utc_datetime_current+'&StartTime='+time_utc_datetime_prev+'&EndTime='+time_utc_datetime_current+'&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C')
    if(response.status_code == 200):
        latest = response.content
        latest = json.loads(latest)
        latest = latest[0]
        if(latest["Open"]!=0 and latest["Close"]!=0 and latest["Low"]!=0 and latest["High"]!=0 ):
            if(HA_Close_latest == 0):  
                HA_Open_latest = (1320.978+1319.854) /2
            else:
                HA_Open_latest = (HA_Open_latest+HA_Close_latest)/2
            HA_Close_latest = (latest["Open"] + latest["Close"] +  latest["Low"] + latest["High"]) /4
            account_sid = 'ACe4f8a304ab7204bd3adb16decbf35e28'
            auth_token = '7eaaeaac35ee2382a51906c6684a03a0'
            client = Client(account_sid, auth_token)
            if (HA_Open_latest < HA_Close_latest):
                message = client.messages.create(
                                        body="Buy",
                                        from_="+13612382106",
                                        to="+971567515767"
                                    )
            else:
                message = client.messages.create(
                                        body="Sell",
                                        from_="+13612382106",
                                        to="+971567515767"
                                    )

def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)  

if __name__ == '__main__':
    schedule.every().day.at("01:00").do(sms)
    schedule.every().day.at("03:00").do(sms)
    schedule.every().day.at("05:00").do(sms)
    schedule.every().day.at("07:00").do(sms)
    schedule.every().day.at("09:00").do(sms)
    schedule.every().day.at("11:00").do(sms)
    schedule.every().day.at("13:00").do(sms)
    schedule.every().day.at("15:00").do(sms)
    schedule.every().day.at("17:00").do(sms)
    schedule.every().day.at("19:00").do(sms)
    schedule.every().day.at("21:00").do(sms)
    schedule.every().day.at("23:00").do(sms)
    t = Thread(target=run_schedule)
    t.start()
    app.run(host='0.0.0.0', port=5000)
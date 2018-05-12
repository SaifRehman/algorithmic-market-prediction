# Algorithmic-market-prediction

<h1 align="center">
  <br>
  <a href="https://github.com/SaifRehman/algorithmic-market-prediction.git"><img src="https://i.ytimg.com/vi/fv5Uk37457M/maxresdefault.jpg" alt="" width=""></a>
  <br>
      Algorthmic Prediction
  <br>
  <br>
</h1>

<h4 align="center">Implementation of Algorthmic Prediction of Candle Patterns</h4>

<p align="center">
  <a>
    <img src="https://img.shields.io/travis/keppel/lotion/master.svg"
         alt="Travis Build">
  </a>
</p>
<br>

## Implemantions 
- [x] Twilio Support
- [x] Heikin Ashi
- [ ] Bullish Harami
- [ ] Bearish Harami
- [ ] Hammer Reversal
- [ ] Doji Candlestick
- [ ] Golang support 

## Heikin Ashi

## What is Heikin Ashi? 
> Heikin-Ashi Candlesticks are an offshoot from Japanese candlesticks. Heikin-Ashi Candlesticks use the open-close data from the prior period and the open-high-low-close data from the current period to create a combo candlestick. The resulting candlestick filters out some noise in an effort to better capture the trend. In Japanese, Heikin means “average” and ashi means “pace” (EUDict.com).

#### Difference between normal candles and Heikin Ashi candles

![1](images/1.png)

> Heiken Ashi candlestick filters out some noise in an effort to better capture the trend. For those that use trailing stops and are trend traders, flipping back between the two candlestick charts is quintessential for traders. In the chart I showed how a trader could use trailing stops to profit from the biggest trends. He or she would set stops with long or short positions and use the previous Heiken Ashi candlestick (green or red - lower or higher) as a gauge to stay in a trade or to get out of a trade. Overal Heiken Ashi is a chart I will look at often to know if I'm on the right side of the trade. 

### Implementation of Heikin Ashi Prediction to Alert you with SMS to bid for buy or sell

This is a Twilio SMS app with background cron jobs for every day 2 hours, inorder to alert for buy or sell 

![2](images/2.png)

1. Create a Account in [Twilio](https://www.twilio.com/console)
2. Create a Account in [IBM Cloud](http://ibm.biz/ioblockchain)
3. Get ```account_sid``` and ```auth_token```
4. Regitser you sms number in twilio 
5. Give a unique name in ```manifest.yml```
6. Push the app to IBM Cloud
```
$ cf push
```

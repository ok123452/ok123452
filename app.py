#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('3bG+w2hW7BANHLOhCw2N10C9qCFW70XcoYcx29wEembHnDUqVG4E7tBC+mmu9d6geT5d11qUHM3JiONllp0/xoVS34O5kME9cahaUWwRtZJxQ7wPbp7mJhMBpYidkRnlRXpPmGsJV2wF2EkfOMx9fAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('f2b5f68345dde00bc44e12b1be42ed6b')

line_bot_api.push_message('U873caf1766f170cb79517c7612140c89', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
import time
import urllib.request as request
from bs4 import BeautifulSoup as sp
import requests
import requests
res = requests.get('https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%222330.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true')
res
<Response [200]>
jd = res.json()['data']
close = jd[0]['chart']['indicators']['quote'][0]['close']
timestamp = jd[0]['chart']['timestamp']
import pandas
df = pandas.DataFrame({'timestamp': timestamp, 'close':close})
df.head()
df['dt'] = pandas.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')
df.plot('dt', 'close', figsize = [20,10])
<matplotlib.axes._subplots.AxesSubplot at 0x139b20da0>


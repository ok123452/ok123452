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

# LineNotify
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def message(mes):
    if __name__ == "__main__":
        token = '權杖' ###
        message = ("\n"+mes)
        lineNotifyMessage(token, message)

#set price
set_price=("1643") ###到價通知

#standard
i=0
def standard(gold_in,note):
    global i
    global st
    global set_price
    if i==0:
        i+=1
    elif gold_in==set_price:
        message(note)
    st=gold_in

#function
j=0
while j==0:
    local_time = time.ctime(time.time())
    url="https://rate.bot.com.tw/gold?Lang=zh-TW" ###
    with request.urlopen(url) as response :
        data=response.read().decode("utf-8")
    root=sp(data,"html.parser")
    gold_in=(root.find_all("td")[5].text.replace("回售","").strip()) ###
    gold_out=(root.find_all("td")[2].text.replace("買進","").strip()) ###
    s1=("\nGold"+"\n銀行買進: "+gold_in+"\n銀行賣出: "+gold_out) ###
    note=local_time+s1
    standard(gold_in,note)
    time.sleep(1) ###

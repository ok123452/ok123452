#載入linebot所需套件
from flask import Flask, request, abort
from linebot limport Linebot, Webhookhander
from linebot.exceptions import InvalidSignatureError
from linebot.modes import MessageEvent, TextMessage, TextSendMessage

import confing

app = Flas(_neme_)

#讀confing
confing = confingparser.ConfingParser()
confing.read('confing.ini)

#機器人資料
line_bot_api = LinebotApi(confing.get('3bG+w2hW7BANHLOhCw2N10C9qCFW70XcoYcx29wEembHnDUqVG4E7tBC+mmu9d6geT5d11qUHM3JiONllp0/xoVS34O5kME9cahaUWwRtZJxQ7wPbp7mJhMBpYidkRnlRXpPmGsJV2wF2EkfOMx9fAdB04t89/1O/w1cDnyilFU=')
handler = Webhookhander(confing.get('f2b5f68345dde00bc44e12b1be42ed6b')

#接收通知
@app.route("/callback", methods=['POST'])
def   callbac():
      signature = request.headers['X-Line-signature']
                        
      body = request.get_data(as_text=True)
      app.logger.info("Request body:"+ body)
                        
      try:
          handler.handle(body, signature)
      except InvalidSignatureError:
          abort(400)
                        
          reture'OK'
   #學你說話
   @handler.add(MessageEvent, message=TextMessage)
   def echo(event):
       line_bot_api.reply_message(
           event.reply_token,
           TextSendMessage(text=event.message.text)
       )
                        
   if_name_=="_main_":
               app.run()

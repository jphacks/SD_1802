# LINE Bot のTest

# import module
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


# 中身
app = Flask(__name__)

line_bot_api = LineBotApi('Access Token')
handler = WebhookHandler('Channel Secret')

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="event.message.text"))


if __name__ == "__main__":
    app.run()

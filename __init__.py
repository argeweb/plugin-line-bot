#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/11
from argeweb import ViewDatastore
from argeweb import ViewFunction
from argeweb.core.events import on
from .libs.linebot.models import TextSendMessage
from .libs.linebot import LineBotApi, WebhookParser
from .models.line_bot_model import LineBotModel
from .models.config_model import ConfigModel


@on('send_line_push_message')
def send_line_push_message(controller, message, to, *args, **kwargs):
    config = ConfigModel.get_config()
    line_bot_api = LineBotApi(config.channel_access_token)
    # parser = WebhookParser(config.channel_secret)
    text_message = TextSendMessage(
        text=message
    )
    line_bot_api.push_message(to, text_message)
    return


plugins_helper = {
    'title': u'Line Bot',
    'desc': u'Line 訊息回覆機器人',
    'controllers': {
        'line_bot': {
            'group': u'Line Bot',
            'actions': [
                {'action': 'list', 'name': u'Line Bot 訊息'},
                {'action': 'add', 'name': u'新增訊息'},
                {'action': 'edit', 'name': u'編輯訊息'},
                {'action': 'view', 'name': u'檢視訊息'},
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        }
    }
}

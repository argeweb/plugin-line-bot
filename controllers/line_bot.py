#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/11

from argeweb import Controller, scaffold
from argeweb import route_with, route_menu, route
from ..models.config_model import ConfigModel
from ..models.line_bot_model import LineBotModel, learn
from ..models.line_bot_input_model import LineBotInputModel
from ..libs.linebot import LineBotApi, WebhookParser
from ..libs.linebot.exceptions import InvalidSignatureError
from ..libs.linebot.models import *


class LineBot(Controller):
    class Scaffold:
        display_in_list = ['title', 'source_type', 'message_type', 'return_message_type', 'py_code', 'weights']

    @route
    @route_menu(list_name=u'backend', group=u'互動項目', text=u'Line Bot 訊息', sort=801)
    def admin_list(self):
        return scaffold.list(self)

    @route
    @route_menu(list_name=u'backend', group=u'互動項目', text=u'Line callback Test', sort=803)
    def callback(self):
        config = ConfigModel.get_config()
        line_bot_api = LineBotApi(config.channel_access_token)
        parser = WebhookParser(config.channel_secret)
        signature = self.request.headers['X-Line-Signature']

        body = self.request.body
        self.logging.info("Request body: " + body)

        # def listening(next_step):
        #     n = LineBotInputModel.get_or_create_by_name(sender, next_step)
        #     n.put()

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            self.abort(400)

        for event in events:
            search_item = None
            return_text = None
            return_original_content_url = None
            return_preview_image_url = None
            return_template = None
            return_alt_text = None
            reply_message = None
            input_item = None
            input_next_step = ''
            user_message = ''
            keyword = ''
            sender = event.source.sender_id
            if event.type == 'message':
                if event.message.type == 'sticker':
                    user_message = event.message.sticker_id
                else:
                    user_message = event.message.text
                input_item = LineBotInputModel.get_by_name(sender)
                if input_item:
                    input_item.need_delete = True
                    input_next_step = input_item.next_step
                    keyword = u'title = (%s) AND (message_type = %s) AND (source_type = input)' % \
                              (input_next_step, event.message.type)
                else:
                    keyword = u'title = (%s) AND (message_type = %s) AND (source_type = %s)  OR (source_type = all)' % \
                              (user_message, event.message.type, event.source.type)
            else:
                if event.type == 'postback':
                    keyword = event.postback.data
                    keyword = u'title = (%s) AND (message_type = %s) AND (source_type = %s)' % (keyword, event.type, event.source.type)
            if not keyword:
                return 'OK'
            search_list = self.components.search('auto_ix_LineBotModel', keyword, sort_field='weights',
                                                 sort_direction='desc', sort_default_value=0.0001)
            if search_list and len(search_list) > 0:
                search_item = search_list[0]
            line_body = body
            line_event = event
            return_message_type = u'TextSendMessage'
            if search_item is not None:
                self.logging.info(search_item)
                return_message_type = search_item.return_message_type
                search_item.weights += 1
                try:
                    exec search_item.py_code
                except Exception as e:
                    self.logging.error(e)
                    return_text = config.onerror_message
                    search_item.weights -= 2
                search_item.put()
            else:
                return_text = config.unknown_message
            if input_item is not None:
                if input_next_step != input_item.next_step:
                    input_item.need_delete = False
                    input_item.user_message = user_message
                    input_item.put()
                if input_item.need_delete is True:
                    input_item.key.delete()
            if return_message_type == u'TextSendMessage':
                if return_text and not return_text.strip() == u'':
                    reply_message = TextSendMessage(
                        text=return_text
                    )
            if return_message_type == u"ImageSendMessage":
                if return_original_content_url and return_preview_image_url:
                    reply_message = ImageSendMessage(
                        original_content_url=return_original_content_url,
                        preview_image_url=return_preview_image_url
                    )
            if return_message_type == u"TemplateSendMessage":
                if return_template:
                    reply_message = TemplateSendMessage(
                        alt_text=return_alt_text,
                        template=return_template
                    )
            if reply_message:
                line_bot_api.reply_message(event.reply_token, reply_message)
        return 'OK'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/11

from google.appengine.api import namespace_manager
from argeweb import Controller, scaffold
from argeweb import route_with, route_menu, route
from google.appengine.api import memcache
import datetime
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
from ..models.line_bot_config_model import LineBotConfigModel

from ..libs.linebot import (
    LineBotApi, WebhookParser
)
from ..libs.linebot.exceptions import (
    InvalidSignatureError
)
from ..libs.linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, JoinEvent, LeaveEvent, FollowEvent, UnfollowEvent,
    StickerMessage, BeaconEvent, PostbackEvent
)


class LineBot(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)
        pagination_limit = 50

    class Scaffold:
        display_in_list = ['title', 'source_type', 'message_type', 'return_message_type', 'py_code']

    @route
    @route_menu(list_name=u'backend', text=u'Line Bot 訊息', sort=801, group=u'互動項目')
    def admin_list(self):
        return scaffold.list(self)

    @route
    @route_menu(list_name=u'backend', text=u'Line callback Test', sort=803, group=u'互動項目')
    def callback(self):
        config = LineBotConfigModel.find_or_create_by_name(self.namespace)
        line_bot_api = LineBotApi(config.channel_access_token)
        parser = WebhookParser(config.channel_secret)
        signature = self.request.headers['X-Line-Signature']

        # get request body as text
        body = self.request.body
        self.logging.info("Request body: " + body)

        # parse webhook body
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            self.abort(400)

        # if event is MessageEvent and message is TextMessage, then echo text
        for event in events:
            return_message = None
            search_item = None
            if isinstance(event, JoinEvent):
                return_message = config.join_event_message
            if isinstance(event, LeaveEvent):
                pass
            if isinstance(event, FollowEvent):
                return_message = config.follow_event_message
            if isinstance(event, UnfollowEvent):
                pass
            if isinstance(event, StickerMessage):
                pass
            if isinstance(event, BeaconEvent):
                pass
            if isinstance(event, PostbackEvent):
                pass
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
                user_message = event.message.text
                keyword = event.message.text + u' AND (message_type = %s ) AND (source_type = %s)' % (event.type, event.source.type)
                self.logging.info(keyword)
                search_list = self.components.search('auto_ix_LineBotModel', keyword)
            self.logging.info(search_list)
            if len(search_list) > 0:
                search_item = search_list[0]
            if search_item:
                self.logging.info(search_item)
                line_body = body
                line_event = event
                exec search_item.py_code

                self.logging.info(return_message)
                if search_item.return_message_type == u'TextSendMessage':
                    if return_message and not return_message.strip() == u'':
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=return_message)
                        )

        return 'OK'
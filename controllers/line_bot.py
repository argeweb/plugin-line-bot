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
from argparse import ArgumentParser

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
        display_in_list = ('site_name', 'domain_expiration_date',
                                      'space_expiration_date', 'contact_person',
                                      'contact_telephone', 'contact_mobile', 'host',)

    @route
    @route_menu(list_name=u'backend', text=u'Line callback Test', sort=999999, need_hr=True)
    def callback(self):
        config = self.meta.Model.find_or_create_by_name(self.namespace)
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
            rn = None
            if isinstance(event, JoinEvent):
                rn = u"我來了"
            if isinstance(event, LeaveEvent):
                rn = u"再會"
            if isinstance(event, FollowEvent):
                rn = u"解開束縛"
            if isinstance(event, UnfollowEvent):
                rn = u"不~~別鎖我"
            if isinstance(event, StickerMessage):
                rn = u"StickerMessage"
            if isinstance(event, BeaconEvent):
                rn = u"BeaconEvent"
            if isinstance(event, PostbackEvent):
                rn = u"PostbackEvent"
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
                rn = event.message.text[::-1]
            if rn:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=rn)
                )

        return 'OK'
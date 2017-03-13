#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/2/23.

from argeweb import BasicModel
from argeweb import Fields


class LineBotConfigModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'系統編號')
    title = Fields.StringProperty(verbose_name=u'Line Bot 名稱', default=u'Arge')
    channel_secret = Fields.StringProperty(verbose_name=u'channel_secret', default=u'')
    channel_access_token = Fields.StringProperty(verbose_name=u'channel_access_token', default=u'')
    unknown_message = Fields.StringProperty(verbose_name=u'無法判斷時', default=u'')
    join_event_message = Fields.StringProperty(verbose_name=u'JoinEventMessage', default=u'')
    join_event_code = Fields.TextProperty(verbose_name=u'JoinEventCode', default=u'')
    follow_event_message = Fields.StringProperty(verbose_name=u'FollowEventMessage', default=u'')
    follow_event_code = Fields.TextProperty(verbose_name=u'FollowEventCode', default=u'')


    @classmethod
    def find_or_create_by_name(cls, name):
        item = cls.find_by_name(name)
        if item is None:
            item = cls()
            item.name = name
            item.put()
        return item
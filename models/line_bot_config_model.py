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
    title = Fields.StringProperty(default=u'Line Bot 名稱', verbose_name=u'Line Bot 名稱')
    channel_secret = Fields.StringProperty(default=u'', verbose_name=u'channel_secret')
    channel_access_token = Fields.StringProperty(default=u'', verbose_name=u'channel_access_token')

    @classmethod
    def find_or_create_by_name(cls, name):
        item = cls.find_by_name(name)
        if item is None:
            item = cls()
            item.name = name
            item.put()
        return item
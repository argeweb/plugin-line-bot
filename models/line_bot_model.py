#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/2/23.

from argeweb import BasicModel
from argeweb import Fields


def learn(keyword, message, weights=1):
    item = LineBotModel()
    item.title = keyword
    item.py_code = 'return_text = u"""%s"""' % message
    item.weights = weights
    item.put()

class LineBotModel(BasicModel):
    title = Fields.TextProperty(verbose_name=u'檢查的字串', default=u'')
    py_code = Fields.TextProperty(verbose_name=u'PyCode', default=u'')
    source_type = Fields.StringProperty(verbose_name=u'要處理的訊息來源', default=u'user', choices=(
        u'user',
        u'group',
        u'room',
        u'input',
        u'all',
    ))
    message_type = Fields.StringProperty(verbose_name=u'要處理的訊息類型', default=u'text', choices=(
        u'text',
        u'image',
        u'video',
        u'audio',
        u'location',
        u'sticker',
        u'follow',
        u'unfollow',
        u'join',
        u'leave',
        u'postback',
    ))
    return_message_type = Fields.StringProperty(verbose_name=u'回傳的訊息類型', default=u'TextSendMessage', choices=(
        u'TextSendMessage',
        u'ImageSendMessage',
        u'TemplateSendMessage',
    ))
    weights = Fields.FloatProperty(verbose_name=u'權重', default=0.0)

    @classmethod
    def get_or_create_by_name(cls, name):
        item = cls.get_by_name(name)
        if item is None:
            import time
            item = cls()
            item.name = name
            item.weights = time.time()
            item.put()
        return item
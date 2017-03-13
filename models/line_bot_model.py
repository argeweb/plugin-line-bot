#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/2/23.

from argeweb import BasicModel
from argeweb import Fields


class LineBotModel(BasicModel):
    name = Fields.HiddenProperty(verbose_name=u'系統編號')
    title = Fields.TextProperty(verbose_name=u'檢查的字串', default=u'')
    py_code = Fields.TextProperty(verbose_name=u'PyCode', default=u'')
    source_type = Fields.StringProperty(verbose_name=u'要處理的訊息來源', default=u'user')
    message_type = Fields.StringProperty(verbose_name=u'要處理的訊息類型', default=u'message')
    return_message_type = Fields.StringProperty(verbose_name=u'回傳的訊息類型', default=u'TextSendMessage')

    @classmethod
    def find_or_create_by_name(cls, name):
        item = cls.find_by_name(name)
        if item is None:
            item = cls()
            item.name = name
            item.put()
        return item
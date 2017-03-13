#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/2/23.

from argeweb import BasicModel
from argeweb import Fields


def wait_input(user_id, next_setp):
    return LineBotInputModel.find_or_create_by_name(user_id, next_setp)


class LineBotInputModel(BasicModel):
    name = Fields.HiddenProperty(verbose_name=u'userId')
    next_step = Fields.StringProperty(verbose_name=u'下一步', default=u'')

    @classmethod
    def find_or_create_by_name(cls, name, next_step):
        item = cls.find_by_name(name)
        if item is None:
            item = cls()
            item.name = name
            item.next_step = next_step
            item.put()
        return item
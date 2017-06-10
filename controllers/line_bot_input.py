#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/11

from argeweb import Controller, scaffold
from argeweb import route_with, route_menu, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search


class LineBotInput(Controller):
    @route
    @route_menu(list_name=u'backend', text=u'Line Input', sort=801, group=u'互動項目')
    def admin_list(self):
        return scaffold.list(self)

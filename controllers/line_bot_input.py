#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/11

from argeweb import Controller, scaffold, route_menu, route


class LineBotInput(Controller):
    @route
    @route_menu(list_name=u'backend', group=u'互動項目', text=u'Line Input', sort=801)
    def admin_list(self):
        return scaffold.list(self)

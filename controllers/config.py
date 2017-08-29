#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/2/23.

from argeweb import Controller, scaffold, route_menu, route


class Config(Controller):
    @route
    @route_menu(list_name=u'backend', group=u'互動項目', text=u'Line Bot 設定', sort=802)
    def admin_config(self):
        config_record = self.meta.Model.get_or_create_by_name('line_bot')
        return scaffold.edit(self, config_record.key)

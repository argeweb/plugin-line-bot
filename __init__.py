#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/11
from argeweb import ViewDatastore
from argeweb import ViewFunction


plugins_helper = {
    'title': u'Line Bot',
    'desc': u'Line 訊息回覆機器人',
    'controllers': {
        'line_bot': {
            'group': u'Line Bot',
            'actions': [
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        }
    }
}

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..appium_page_objects import PageObject, page_element

class HomePage(PageObject):
	# navigation bar
	gerenzhongxin_button = page_element(accessibility_id = "个人中心")
	feivip_button = page_element(accessibility_id = "非vip")
	qiehuanyejianmoshi_button = page_element(accessibility_id = "切换到夜间模式")
	sousuo_button = page_element(accessibility_id = "搜索")





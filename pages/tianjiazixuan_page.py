#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element


class TianjiazixuanPage(PageObject):
	fanhui_button = page_element(accessibility_id = '返回')
	tianjiazixuan_staticText = page_element(xpath= "//UIAStaticText[@name='添加自选']")

	zixuanadd_button = page_element(accessibility_id = 'zixuan add')

	qingchuwenben_button = page_element(accessibility_id = '清除文本')


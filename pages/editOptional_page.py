#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element


class EditOptionalPage(PageObject):
	fanhui_button = page_element(accessibility_id = "返回")
	bianjizixuan_StaticText = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')
	tianjiagupiao_button = page_element(accessibility_id = "添加股票")

	PFYH_button = page_element(accessibility_id = "浦发银行")
	PAYH_button = page_element(accessibility_id = "平安银行")
	YSBG_button = page_element(accessibility_id = "云赛Ｂ股")





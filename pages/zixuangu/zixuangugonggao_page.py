#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixuangugonggaoPage(PageObject):
	fanhui_btn = page_element(accessibility_id = '返回')
	zixuangugonggao_staText = page_element(xpath = "//UIAStaticText[@name= '自选股公告']")

	cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
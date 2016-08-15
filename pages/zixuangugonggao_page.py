#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..appium_page_objects import PageObject, page_element

class ZixuangugonggaoPage(PageObject):
	fanhui_btn = page_element(accessibility_id = '返回')
	zixuangugonggao_staText = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')

	cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
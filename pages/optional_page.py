#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..appium_page_objects import PageObject, page_element

__author__ = "Hemin Won"

class OptionalPage(PageObject):
	# navigation bar
	bianji_button = page_element(accessibility_id = "编辑")
	Zixuan_button = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"
	zixuan_button = page_element(xpath = Zixuan_button)
	sousuo_button = page_element(accessibility_id = "搜索")


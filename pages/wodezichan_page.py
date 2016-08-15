#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class WodezichanPage(PageObject):
	fanhui_btn = page_element(accessibility_id = '返回')
	wodezichan_staText = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')
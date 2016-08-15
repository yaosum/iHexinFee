#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element


class FenshiKxianPage(PageObject):
	fanhui_button = page_element(accessibility_id='返回')
	xiayigegupiao_button = page_element(accessibility_id = '下一个股票')
	shangyigegupiao_button = page_element(accessibility_id = '上一个股票')

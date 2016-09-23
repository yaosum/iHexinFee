#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixuanDapanPage(PageObject):
	hu_btn = page_element(accessibility_id = "btn hu")
	shen_btn = page_element(accessibility_id = "btn shen")
	chuang_btn = page_element(accessibility_id = "btn chuang")

	fenshitu_scr = page_element(xpath= "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]")
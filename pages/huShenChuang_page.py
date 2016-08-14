#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..appium_page_objects import PageObject, page_element

class HuShenChuangPage(PageObject):
	hu_btn = page_element(accessibility_id = "btn hu")
	shen_btn = page_element(accessibility_id = "btn shen")
	chuang_btn = page_element(accessibility_id = "btn chuang")
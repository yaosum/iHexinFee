#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..appium_page_objects import PageObject, page_element


class EditOptionalPage(PageObject):
	fanhui_button = page_element(accessibility_id = "返回")
	bianjizixuan_StaticText = page_element(accessibility_id = "编辑自选")
	tianjiagupiao_button = page_element(accessibility_id = "添加股票")

	PFYH_button = page_element(accessibility_id = "浦发银行")
	PAYH_button = page_element(accessibility_id = "平安银行")
	YSBG_button = page_element(accessibility_id = "云赛Ｂ股")





#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

__author__ = "Hemin Won"

class OptionalPage(PageObject):
	# navigation bar
	bianji_button = page_element(accessibility_id = "编辑")
	Zixuan_staticText = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"
	zixuan_staticText = page_element(xpath = Zixuan_staticText)
	sousuo_button = page_element(accessibility_id = "搜索")

	hu_staticText = page_element(xpath= "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[7]")
	zijin_btn = page_element(accessibility_id = '资金')
	xinwen_btn = page_element(accessibility_id = '新闻')
	gonggao_btn = page_element(accessibility_id='公告')
	zichan_btn = page_element(accessibility_id='资产')

	zuixin_staText = page_element(accessibility_id ="最新")
	zhangfu_staText = page_element(accessibility_id="涨幅")
	zhangdie_staText = page_element(accessibility_id="涨跌")
	zhangsu_staText = page_element(accessibility_id="涨速")
	zongshou_staText = page_element(accessibility_id="总手")
	huanshopu_staText = page_element(accessibility_id="换手")
	liangbi_staText = page_element(accessibility_id='量比')
	shiyingdong_staText = page_element(accessibility_id='市盈(动)')
	shijinglv_staText = page_element(accessibility_id='市净率')
	xianshou_staText = page_element(accessibility_id='现手')
	kaipan_staText = page_element(accessibility_id='开盘')
	zuoshou_staText = page_element(accessibility_id='昨收')
	zuigao_staText = page_element(accessibility_id='最高')
	zuidi_staText = page_element(accessibility_id='最低')
	weibi_staText = page_element(accessibility_id='委比')
	zhenfu_staText = page_element(accessibility_id='振幅')

	quxiaopaixu_btn = page_element(accessibility_id="取消排序")

	shanchu_btn = page_element(accessibility_id="删除")
	zhiding_btn = page_element(accessibility_id="置顶")
	zhidi_btn = page_element(accessibility_id="置底")


	cell001 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
	cell017 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[17]')

	cell001_staText = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')

	def hx_upglide(self):
		# 基于iPhone6 375/667
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (256/375.0)
		start_y = height * (598/667.0)
		end_x = width * (256/375.0)
		end_y = height * (183/667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_glide(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (256 / 375.0)
		start_y = height * (183 / 667.0)
		end_x = width * (256 / 375.0)
		end_y = height * (598/667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_right(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (359 / 375.0)
		start_y = height * (214 / 667.0)
		end_x = width * (164 / 375.0)
		end_y = height * (214 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_left(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (164 / 375.0)
		start_y = height * (214 / 667.0)
		end_x = width * (359 / 375.0)
		end_y = height * (214 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_longPress(self, element):

		location = element.location
		el_size = element.size

		x = el_size['width'] / 2.0 + location['x']
		y = el_size['height'] / 2.0 + location['y']

		return self.w.tap([(x, y)], duration=0.5)

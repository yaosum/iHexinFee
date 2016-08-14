#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from pages.addOptional_page import AddOptionalPage
from pages.editOptional_page import EditOptionalPage
from pages.home_page import HomePage
from pages.huShenChuang_page import HuShenChuangPage
from pages.optional_page import OptionalPage
from pages.public_page import PublicPage
from pages.searchStock_page import SearchStockPage

"""
def test_step001(driver):
	home_page = HomePage(driver)
	assert home_page.gerenzhongxin_button

def test_step002(driver):
	optional_page = OptionalPage(driver)
	PublicPage(driver).zixuan_button.click()
	assert optional_page.zixuan_staticText.text == u'自选'

def test_step003(driver):
	PublicPage(driver).zixuan_button.click()
	OptionalPage(driver).bianji_button.click()
	editOptional_page = EditOptionalPage(driver)
	assert editOptional_page.bianjizixuan_StaticText

def test_step004(driver):
	PublicPage(driver).zixuan_button.click()
	OptionalPage(driver).bianji_button.click()
	EditOptionalPage(driver).tianjiagupiao_button.click()
	addOptional_page = AddOptionalPage(driver)
	assert addOptional_page.tianjiazixuan_staticText.text == u'添加自选'
"""
def test_step005_014(driver):
	public_page = PublicPage(driver)
	addOpyional_page = AddOptionalPage(driver)

	public_page.zixuan_button.click()
	OptionalPage(driver).bianji_button.click()
	editOptional_page = EditOptionalPage(driver)
	editOptional_page.tianjiagupiao_button.click()
	searchStock_page = SearchStockPage(driver)
	sleep(1)
	searchStock_page.hx_send_keys('6','0','0','0','0','0')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('0', '0', '0', '0', '0', '1')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('9', '0', '0', '9', '0', '1')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('2', '0', '0', '0', '1', '1')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('0', '1', '0', '1', '0', '7')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('1', '0', '0', '2', '1', '3')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('5', '0', '0', '0', '3', '8')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('1', '5', '0', '0', '0', '8')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('4', '0', '0', '0', '0', '2')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('3', '9', '9', '0', '0', '1')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('d', 'j', 'i')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('B', 'I', 'D', 'U')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('5', '1', '0', '0', '5', '0')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()

	searchStock_page.hx_send_keys('T', 'J', 'A', 'G', '0', '0')
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()


	searchStock_page.hx_send_keys('0', '0', '0', '0', '1')
	sleep(1)
	addOpyional_page.zixuanadd_button.click()
	addOpyional_page.qingchuwenben_button.click()
	searchStock_page.hx_send_keys('h', 's', 'i')
	sleep(1)
	addOpyional_page.zixuanadd_button.click()

	addOpyional_page.fanhui_button.click()
	assert editOptional_page.PFYH_button
	assert editOptional_page.PAYH_button
	#assert editOptional_page.YSBG_button

	editOptional_page.fanhui_button.click()

	public_page.shouye_button.click()
	public_page.zixuan_button.click()



def test_step20(driver):


	public_page.zixuan_button.click()
	optional_page.sousuo_button.click()
	sleep(1)
	searchStock_page.hx_send_keys('1','A','0','0','0','1')
	searchStock_page.qingchuwenben_button.click()
	searchStock_page.hx_send_keys('3', '9', '9', '0', '0', '6')

def test_step031(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	searchStock_page = SearchStockPage(driver)
	huShenChuang_page = HuShenChuangPage(driver)

	public_page.zixuan_button.click()
	optional_page.hu_staticText.click()
	huShenChuang_page.shen_btn.click()
	huShenChuang_page.chuang_btn.click()




	pass
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from pages import searchStock_page
from pages.tianjiazixuan_page import TianjiazixuanPage
from pages.bianjizixuan_page import BianjizixuanPage
from pages.fenshiKxian_page import FenshiKxianPage
from pages.optional_page import OptionalPage
from pages.public_page import PublicPage
from pages.searchStock_page import SearchStockPage
from pages.home_page import HomePage
from time import sleep

def test_search(driver):
	optional_page = OptionalPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)
	searchStock_page = SearchStockPage(driver)
	bianjizixuan_page = BianjizixuanPage(driver)
	public_page = PublicPage(driver)
	home_page = HomePage(driver)

	public_page.zixuan_button.click()
	# step99
	optional_page.hx_glide()

	sleep(1)
	# assert optional_page.cell001_stock_staText.text == u'同花顺'
	# optional_page.cell001.click()
	optional_page.THS_stock_staText.click()

if __name__ == '__main__':
	# equals to setUp
	desired_caps = {}
	# basic settings
	desired_caps['platformName'] = 'iOS'
	desired_caps['platformVersion'] = '9.3'

	# real device
	desired_caps['deviceName'] = 'iPhone 6'
	desired_caps['udid'] = '57e95712fdd52a1fce030ed46808f1a98e9b2f5e'
	desired_caps['bundleId'] = 'cn.com.10jqka.iHexinFee'
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	test_search(driver)


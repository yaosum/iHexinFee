#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

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
	HomePage(driver).sousuo_button.click()
	sleep(2)
	searchStock_page.hx_send_keys('60sc01')
	pass



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


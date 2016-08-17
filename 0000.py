#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

from pages import searchStock_page
from pages.addOptional_page import AddOptionalPage
from pages.editOptional_page import EditOptionalPage
from pages.fenshiKxian_page import FenshiKxianPage
from pages.optional_page import OptionalPage
from pages.public_page import PublicPage
from pages.searchStock_page import SearchStockPage
from pages.home_page import HomePage
from time import sleep

def test_search(driver):
	optional_page = OptionalPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)
	SearchStockPage(driver)
	PublicPage(driver).zixuan_button.click()
	optional_page.sousuo_button.click()
	searchStock_page.hx_send_keys('1', 'A', '0', '0', '0', '1')
	SearchStockPage.zixuanadd_button.click()
	searchStock_page.qingchuwenben_button.click()
	searchStock_page.hx_send_keys('3', '9', '9', '0', '0', '6')
	fenshikxian_page.jiazixuan_staText.click()
	fenshikxian_page.fanhui_button.click()
	optional_page.sousuo_button.click()
	searchStock_page.hx_send_keys('3', '0', '0', '0', '3', '3')
	fenshikxian_page.jiazixuan_staText.click()
	fenshikxian_page.fanhui_button.click()

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


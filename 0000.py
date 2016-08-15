#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from pages.searchStock_page import SearchStockPage
from pages.home_page import HomePage
from time import sleep

def test_search(driver):

	HomePage(driver).sousuo_button.click()
	sleep(1)
	SearchStockPage(driver).hx_send_keys('123')
	sleep(1)



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


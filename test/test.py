#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Hemin Won"

import os
import unittest
import sys

from appium import webdriver
from time import sleep


class TestOptional(unittest.TestCase):
    def setUp(self):
        # open iHexinFee on iPhone6(9.3)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # real device
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['udid'] = '57e95712fdd52a1fce030ed46808f1a98e9b2f5e'
        desired_caps['bundleId'] = 'cn.com.10jqka.iHexinFee'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_000(self):
		self.driver.find_element_by_accessibility_id("自选").click()
		self.driver.find_element_by_accessibility_id("公告").click()
		self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]").click()
		sleep(2)
		print self.driver.current_context
		print self.driver.contexts
		sleep(2)
		if len(self.driver.contexts) == 1:
			raise AssertionError("Canont find webview")
		webview = self.driver.contexts[-1]
		self.driver.switch_to.context(webview)
		print self.driver.current_context
		print self.driver.page_source
		#self.driver.get("http://www.baidu.com")
		#self.driver.get("http://notice.10jqka.com.cn/api/pdf/6cb255a23e8383f5.pdf")
		#self.driver.find_element_by_link_text("查看原文").click()
		#self.driver.find_element_by_accessibility_id("查看原文").click()
		#self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[3]").click()
		#self.driver.find_element_by_xpath("//UIAStaticText[@name='查看原文']").click()
		sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptional)
    unittest.TextTestRunner(verbosity=2).run(suite)

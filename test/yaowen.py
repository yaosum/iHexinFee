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
		self.driver.find_element_by_accessibility_id("资讯").click()
		self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]").click()
		sleep(3)
		#if len(self.driver.contexts) == 1:
			#raise AssertionError("Cannot find webview")
		#webview = self.driver.contexts[-1]
		#self.driver.switch_to.context(webview)
		self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[5]").click()
		#self.driver.switch_to.context(self.driver.contexts[0])
		sleep(3)



		sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptional)
    unittest.TextTestRunner(verbosity=2).run(suite)


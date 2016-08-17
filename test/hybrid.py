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
        desired_caps['bundleId'] = 'Hm.appiumios.appForUITest1'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_000(self):
		# 进入 WebView 界面
		self.driver.find_element_by_accessibility_id("WebView").click()
		sleep(5)

		# 检查有没有 WebView Context
		if len(self.driver.contexts) == 1:
			raise AssertionError("Cannot find webview")

		# 切换到 WebView Context
		webview = self.driver.contexts[-1]
		self.driver.switch_to.context(webview)

		self.driver.find_element_by_link_text("点击后 testLabel 变成 abc").click()
		sleep(3)
		#print(self.driver.current_context)

		#print "WebView: \n%s" % self.driver.page_source
		#self.driver.save_screenshot("hybrid_webview_real_device.png")

		# 切换回 Native Context
		self.driver.switch_to.context(self.driver.contexts[0])
		self.driver.find_element_by_xpath("//UIAButton[@name='OK']").click()
		#self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]").click()
		print(self.driver.current_context)
		#print "Native: \n%s" % self.driver.page_source
		#self.driver.save_screenshot("hybrid_native_real_device.png")
		self.assertEqual(self.driver.find_element_by_xpath("//UIAStaticText[@name='abc']").text, "abc")
		print(self.driver.current_context)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptional)
    unittest.TextTestRunner(verbosity=2).run(suite)


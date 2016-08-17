#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction


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


    def test_001(self):
		# 放大手势
		el = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[4]")
		assert el.text == u'切换到夜间模式'
		self.driver.find_element_by_accessibility_id("自选").click()
		self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[7]").click()
		self.driver.find_element_by_accessibility_id("btn shen").click()
		self.driver.find_element_by_accessibility_id("btn chuang").click()
		self.driver.swipe(start_x=292, start_y=259, end_x=61, end_y=259, duration=500)
		self.driver.swipe(start_x=61, start_y=259, end_x=292, end_y=259, duration=500)
		self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]").click()
		sleep(1)
		self.driver.swipe(start_x=53, start_y=194, end_x=335, end_y=194, duration=500)
		sleep(2)
		els = self.driver.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[4]/UIAStaticText[1]")

		a1 = TouchAction()
		a1.press(els[0]).move_to(x=40, y=0).move_to(x=40, y=0).release()

		a2 = TouchAction()
		a2.press(els[0]).move_to(x=-40, y=0).move_to(x=-40, y=0).release()

		ma = MultiAction(self.driver, els[0])
		ma.add(a1, a2)
		ma.perform()
		sleep(2)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptional)
    unittest.TextTestRunner(verbosity=2).run(suite)

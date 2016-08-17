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
		self.driver.find_element_by_accessibility_id("自选").click()
		self.driver.find_element_by_accessibility_id("编辑").click()
		cell003_tuodong = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[8]/UIAButton[4]')
		cell001_tuodong = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[4]')
		#self.driver.drag_and_drop(cell003_tuodong, cell001_tuodong)
		a1 = TouchAction(self.driver)
		a1.press(cell003_tuodong).wait(1000).move_to(cell001_tuodong).wait(100).release()
		a1.perform()
		self.driver.find_element_by_accessibility_id("返回").click()
		sleep(2)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptional)
    unittest.TextTestRunner(verbosity=2).run(suite)

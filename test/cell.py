#!/usr/bin/env python
# -*- coding: utf-8 -*-



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

    #def tearDown(self):
        #self.driver.quit()


    def test_001(self):
		self.driver.find_element_by_accessibility_id("自选").click()
		self.driver.find_element_by_accessibility_id("编辑").click()
		#print len(self.driver.find_element_by_xpath("//UIATableCell[@name]"))
		print len(self.driver.find_elements_by_xpath("//UIATableCell[@name]"))



		sleep(2)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptional)
    unittest.TextTestRunner(verbosity=2).run(suite)

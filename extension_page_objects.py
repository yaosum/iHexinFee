#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium_page_objects import PageObject, page_element

class ExtensionPageObject(PageObject):
	def __init__(self, webdriver, accessibility_id_elements=None, xpath_page_elements=None):
		# type: (object, object, object) -> object
		"""
		:param webdriver:
		:param accessibility_id_elements: 字典 element变量名 对应element accessibility_id
		:param xpath_page_elements: 字典 element变量名 对应element xpath
		"""
		super(ExtensionPageObject, self).__init__(webdriver)
		if accessibility_id_elements:
			for key in accessibility_id_elements.keys():
				value = accessibility_id_elements[key]
				self.__dict__[key] = page_element(accessibility_id=value)
		if xpath_page_elements:
			for key in xpath_page_elements.keys():
				value = xpath_page_elements.keys()
				self.__dict__[key] = page_element(xpath=value)


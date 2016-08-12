#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..appium_page_objects import PageObject, page_element

class HomePage(PageObject):
	sousuo_button = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[5]")


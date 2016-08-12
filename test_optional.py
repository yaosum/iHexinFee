#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pages.addOptional_page import AddOptionalPage
from pages.editOptional_page import EditOptionalPage
from pages.home_page import HomePage
from pages.optional_page import OptionalPage
from pages.public_page import PublicPage


def test_step001(driver):
	home_page = HomePage(driver)
	assert home_page.gerenzhongxin_button

def test_step002(driver):
	optional_page = OptionalPage(driver)
	PublicPage(driver).zixuan_button.click()
	assert optional_page.zixuan_staticText.text == u'自选'

def test_step003(driver):
	OptionalPage(driver).bianji_button.click()
	editOptional_page = EditOptionalPage(driver)
	assert editOptional_page.bianjizixuan_StaticText

def test_step004(driver):
	EditOptionalPage(driver).tianjiagupiao_button.click()
	addOptional_page = AddOptionalPage(driver)
	assert addOptional_page.tianjiazixuan_staticText.text == u'添加自选'





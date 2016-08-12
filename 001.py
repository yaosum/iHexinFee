#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .pages.searchStock_page import SearchStockPage
from .pages.home_page import HomePage
from time import sleep

def test_search(driver):

	HomePage(driver).sousuo_button.click()
	sleep(1)
	SearchStockPage(driver).hx_send_keys('a', '4')

	sleep(1)


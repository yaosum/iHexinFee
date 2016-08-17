#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium.webdriver.common.touch_action import TouchAction

from pages.addOptional_page import AddOptionalPage
from pages.denglu_page import DengluPage
from pages.editOptional_page import EditOptionalPage
from pages.fenshiKxian_page import FenshiKxianPage
from pages.home_page import HomePage
from pages.huShenChuang_page import HuShenChuangPage
from pages.kanZhulizijin_page import KanZhulizijinPage
from pages.optional_page import OptionalPage
from pages.public_page import PublicPage
from pages.searchStock_page import SearchStockPage
from pages.wodezichan_page import WodezichanPage
from pages.zixuangugonggao_page import ZixuangugonggaoPage
from pages.zixuanguxinwen_page import ZixuanguxinwenPage
from pages.zixun_page import ZixunPage

"""
def test_step001(driver):
	home_page = HomePage(driver)
	optional_page = OptionalPage(driver)
	editOptional_page = EditOptionalPage(driver)
	addOptional_page = AddOptionalPage(driver)

	assert home_page.gerenzhongxin_button
	PublicPage(driver).zixuan_button.click()
	assert optional_page.zixuan_staticText.text == u'自选'
	optional_page.bianji_button.click()
	assert editOptional_page.bianjizixuan_StaticText.text == u'编辑自选'
	editOptional_page.tianjiagupiao_button.click()
	assert addOptional_page.tianjiazixuan_staticText.text == u'添加自选'
"""

def test_step005(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	addOpyional_page = AddOptionalPage(driver)
	editOptional_page = EditOptionalPage(driver)
	searchStock_page = SearchStockPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)

	public_page.zixuan_button.click()

	optional_page.bianji_button.click()
	editOptional_page.tianjiagupiao_button.click()

	sleep(1)

	searchStock_page.hx_send_keys_with_addStock('6', '0', '0', '0', '0', '0')
	searchStock_page.hx_send_keys_with_addStock('0', '0', '0', '0', '0', '1')
	searchStock_page.hx_send_keys_with_addStock('9', '0', '0', '9', '0', '1')
	searchStock_page.hx_send_keys_with_addStock('2', '0', '0', '0', '1', '1')
	searchStock_page.hx_send_keys_with_addStock('0', '1', '0', '1', '0', '7')
	searchStock_page.hx_send_keys_with_addStock('1', '0', '0', '2', '1', '3')
	searchStock_page.hx_send_keys_with_addStock('5', '0', '0', '0', '5', '8')
	searchStock_page.hx_send_keys_with_addStock('1', '5', '0', '0', '0', '8')
	searchStock_page.hx_send_keys_with_addStock('4', '0', '0', '0', '0', '2')
	searchStock_page.hx_send_keys_with_addStock('3', '9', '9', '0', '0', '1')
	searchStock_page.hx_send_keys_with_addStock('d', 'j', 'i')
	searchStock_page.hx_send_keys_with_addStock('B', 'I', 'D', 'U')
	searchStock_page.hx_send_keys_with_addStock('5', '1', '0', '0', '5', '0')
	searchStock_page.hx_send_keys_with_addStock('T', 'J', 'A', 'G', '0', '0')

	searchStock_page.hx_send_keys_with_addStock('0', '0', '0', '0', '1')
	searchStock_page.hx_send_keys_with_addStock('h', 's', 'i')

	addOpyional_page.fanhui_button.click()
	driver.swipe(start_x=285, start_y=108, end_x=285, end_y=550, duration=500)
	#assert editOptional_page.cell001_staText.text == u'现货白银'
	editOptional_page.fanhui_button.click()
	sleep(1)
	print optional_page.cell001.text
	#assert optional_page.cell001_staText.text == u'现货白银'
	public_page.shouye_button.click()
	public_page.zixuan_button.click()
	optional_page.bianji_button.click()
	driver.swipe(start_x=285, start_y=548, end_x=285, end_y=117, duration=500)
	#置顶三次操作
	editOptional_page.cell017_zhiding_btn.click()
	editOptional_page.cell017_zhiding_btn.click()
	editOptional_page.cell017_zhiding_btn.click()
	# 第一条为上证指数
	driver.swipe(start_x=285, start_y=108, end_x=285, end_y=550, duration=500)
	assert editOptional_page.cell001_staText.text == u'上证指数'
	editOptional_page.fanhui_button.click()
	#
	#optional_page.cell001_staText.text == u'上证指数'
	optional_page.bianji_button.click()
	action1 = TouchAction(driver)
	action1.press(editOptional_page.cell002_tuodong_btn).wait(100).move_to(editOptional_page.cell001_tuodong_btn).wait(100).release()
	action1.perform()
	action2 = TouchAction(driver)
	action2.press(editOptional_page.cell003_tuodong_btn).wait(100).move_to(editOptional_page.cell001_tuodong_btn).wait(100).release()
	action2.perform()
	editOptional_page.fanhui_button.click()
	#assert optional_page.cell001_staText.text == u'同花顺'

	optional_page.bianji_button.click()
	editOptional_page.cell001_btn.click()
	editOptional_page.cell002_btn.click()
	editOptional_page.cell003_btn.click()
	editOptional_page.shanchu_button.click()
	editOptional_page.fanhui_button.click()
	sleep(2)

	optional_page.sousuo_button.click()
	searchStock_page.hx_send_keys('1','A','0','0','0','1')
	SearchStockPage.zixuanadd_button.click()
	searchStock_page.qingchuwenben_button.click()
	searchStock_page.hx_send_keys('3','9','9','0','0','6')
	fenshikxian_page.jiazixuan_staText.click()
	fenshikxian_page.fanhui_button.click()
	optional_page.sousuo_button.click()
	searchStock_page.hx_send_keys('3', '0', '0', '0', '3', '3')
	fenshikxian_page.jiazixuan_staText.click()
	fenshikxian_page.fanhui_button.click()

	# step89
	# 上滑
	optional_page.hx_upglide()
	optional_page.hx_upglide()
	optional_page.hx_glide()
	optional_page.hx_glide()
	optional_page.hx_glide()
	# 左滑
	optional_page.hx_right()
	optional_page.hx_right()
	optional_page.hx_right()
	optional_page.hx_right()
	optional_page.hx_right()
	optional_page.hx_right()
	optional_page.hx_right()
	optional_page.hx_right()

	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()
	optional_page.hx_left()

	optional_page.zuixin_staText.click()
	optional_page.zuixin_staText.click()
	optional_page.quxiaopaixu_btn.click()


	# 待添加


	optional_page.zhenfu_staText.click()
	optional_page.zhenfu_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zhangfu_staText.click()
	optional_page.zhangfu_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zuixin_staText.click()
	optional_page.zuixin_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.cell001.click()
	sleep(1)
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click

	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()

	fenshikxian_page.hx_left()

	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click
	fenshikxian_page.xiayigegupiao_button.click

	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()
	fenshikxian_page.shangyigegupiao_button.click()

	fenshikxian_page.fanhui_button.click()

	optional_page.zuixin_staText.click()
	optional_page.hx_longPress(optional_page.cell001)
	optional_page.zhidi_btn.click()
	# 待扩展
	optional_page.quxiaopaixu_btn.click()
	optional_page.zuixin_staText.click()
	optional_page.hx_upglide()
	optional_page.hx_longPress(optional_page.cell017)
	optional_page.zhiding_btn.click()
	optional_page.quxiaopaixu_btn.click()
	optional_page.hx_glide().click()
	optional_page.hx_longPress(optional_page.cell001)
	optional_page.shanchu_btn.click()
	optional_page.hx_longPress(optional_page.cell001)
	optional_page.shanchu_btn.click()






"""
def test_step031(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	searchStock_page = SearchStockPage(driver)
	huShenChuang_page = HuShenChuangPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)

	public_page.zixuan_button.click()
	optional_page.hu_staticText.click()
	huShenChuang_page.shen_btn.click()
	huShenChuang_page.chuang_btn.click()
	driver.swipe(start_x=300, start_y=239, end_x=39, end_y=239, duration=500)
	huShenChuang_page.shen_btn.click()
	huShenChuang_page.hu_btn.click()
	driver.swipe(start_x=39, start_y=239, end_x=300, end_y=239, duration=500)
	driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 188, "y": 480})
	optional_page.hu_staticText.click()
	huShenChuang_page.shen_btn.click()
	driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 188, "y": 480})
	optional_page.hu_staticText.click()
	huShenChuang_page.chuang_btn.click()
	driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 188, "y": 480})
	optional_page.hu_staticText.click()
	huShenChuang_page.fenshitu_scr.click()
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	driver.swipe(start_x=331, start_y=296, end_x=59, end_y=296, duration=500)
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	driver.swipe(start_x=59, start_y=296, end_x=331, end_y=296, duration=500)
	fenshikxian_page.fanhui_button.click()

def test_step051(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	searchStock_page = SearchStockPage(driver)
	huShenChuang_page = HuShenChuangPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)
	kanzhulizijin_page = KanZhulizijinPage(driver)
	denglu_page = DengluPage(driver)

	public_page.zixuan_button.click()
	optional_page.zijin_btn.click()
	kanzhulizijin_page.denglu_btn.click()
	denglu_page.guanbi_btn.click()
	kanzhulizijin_page.hushen_btn.click()
	# 上下滑
	driver.swipe(start_x=304, start_y=598, end_x=304, end_y=154, duration=500)
	driver.swipe(start_x=304, start_y=154, end_x=304, end_y=598, duration=500)

	# 左右滑
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)

	driver.swipe(start_x=142, start_y=466, end_x=358, end_y=466, duration=500)
	driver.swipe(start_x=142, start_y=466, end_x=358, end_y=466, duration=500)
	driver.swipe(start_x=142, start_y=466, end_x=358, end_y=466, duration=500)

	kanzhulizijin_page.hx_ergodic_hushen_zhibiao()

	kanzhulizijin_page.hangye_btn.click()
	kanzhulizijin_page.hx_ergodic_zhibiao()

	kanzhulizijin_page.gainian_btn.click()
	kanzhulizijin_page.hx_ergodic_zhibiao()

	kanzhulizijin_page.fanhui_btn.click()
"""
"""
def test_step69(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	searchStock_page = SearchStockPage(driver)
	huShenChuang_page = HuShenChuangPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)
	zixuanguxinwen_page = ZixuanguxinwenPage(driver)
	zixun_page = ZixunPage(driver)

	public_page.zixuan_button.click()
	optional_page.xinwen_btn.click()
	assert zixuanguxinwen_page.zixuanguxinwen_staText
	driver.swipe(start_x=85, start_y=584, end_x=85, end_y=112, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	zixuanguxinwen_page.cell01.click()
	zixun_page.fanhui_btn.click()
	zixuanguxinwen_page.yanbao_btn.click()
	driver.swipe(start_x=85, start_y=584, end_x=85, end_y=112, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	zixuanguxinwen_page.cell01.click()
	zixun_page.fanhui_btn.click()
	zixuanguxinwen_page.fanhui_btn.click()
"""
"""
def test_step80(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	zixuangugonggao_page=ZixuangugonggaoPage(driver)
	zixun_page = ZixunPage(driver)

	public_page.zixuan_button.click()
	optional_page.gonggao_btn.click()
	assert zixuangugonggao_page.zixuangugonggao_staText.text == u'自选股公告'
	driver.swipe(start_x=86, start_y=584, end_x=86, end_y=112, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	zixuangugonggao_page.cell01.click()

	zixun_page.fanhui_btn.click()
	zixuangugonggao_page.fanhui_btn.click()

def test_step88(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	zixuangugonggao_page = ZixuangugonggaoPage(driver)
	zixun_page = ZixunPage(driver)
	wodezichan_page = WodezichanPage(driver)

	public_page.zixuan_button.click()
	optional_page.zichan_btn.click()
	wodezichan_page.fanhui_btn.click()

"""
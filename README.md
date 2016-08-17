# iHexin

unittest
```
self.driver.swipe(start_x=279, start_y=205, end_x=88, end_y=205, duration=500)
```

pytest_POM
```
driver.swipe(start_x=300, start_y=239, end_x=39, end_y=239, duration=500)
```
### 手势源码参考

放大
```
els = self.driver.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[4]/UIAStaticText[1]")

		a1 = TouchAction()
		a1.press(els[0]).move_to(x=40, y=0).move_to(x=40, y=0).release()

		a2 = TouchAction()
		a2.press(els[0]).move_to(x=-40, y=0).move_to(x=-40, y=0).release()

		ma = MultiAction(self.driver, els[0])
		ma.add(a1, a2)
		ma.perform()
```
拖动股票
```
a1 = TouchAction(self.driver)
		a1.press(cell003_tuodong).wait(1000).move_to(cell001_tuodong).wait(100).release()
		a1.perform()
```
### 命名规则
1. 页面:对于有一个新page生成需创建一个新page,优先使用标题栏命名,若标题会改变则根据页面功能进行命名
2. 元素:数字开头的元素统一将数字放在末尾
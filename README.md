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
获取屏幕宽高
[ios simulator python 滑动怎么解决，求指导](https://testerhome.com/topics/3703)
```
		self.driver.get_window_size()
		print self.driver.get_window_size()
		print self.driver.get_window_size().get('width')
```
拖动股票
[appium Android 如何实现长按应用图标拖动到删除控件处执行删除操作](https://testerhome.com/topics/5346)
```
a1 = TouchAction(self.driver)
		a1.press(cell003_tuodong).wait(1000).move_to(cell001_tuodong).wait(100).release()
		a1.perform()
```
滑动手势封装
```
	def hx_left(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (344 / 375.0)
		start_y = height * (134 / 667.0)
		end_x = width * (67 / 375.0)
		end_y = height * (134 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)
```
长按手势封装
```
	def hx_longPress(self, element):
		
		location = element.location
		el_size = element.size

		x = el_size['width'] / 2.0 + location['x']
		y = el_size['height'] / 2.0 + location['y']

		return self.w.tap([(x, y)], duration=0.5)

```
滑动
```
def scroll(self, origin_el, destination_el):
        """Scrolls from one element to another

        :Args:
         - originalEl - the element from which to being scrolling
         - destinationEl - the element to scroll to

        :Usage:
            driver.scroll(el1, el2)
        """
        action = TouchAction(self)
        action.press(origin_el).move_to(destination_el).release().perform()
        return self
```
xpath查找元素的问题
```
self.driver.find_element_by_xpath("//UIAStaticText[@name='同花顺']").click()
```
拖动
```
    def drag_and_drop(self, origin_el, destination_el):
        """Drag the origin element to the destination element

        :Args:
         - originEl - the element to drag
         - destinationEl - the element to drag to
        """
        action = TouchAction(self)
        action.long_press(origin_el).move_to(destination_el).release().perform()
        return self
```

### 命名规则
1. 页面:对于有一个新page生成需创建一个新page,优先使用标题栏命名,若标题会改变则根据页面功能进行命名
2. 元素:数字开头的元素统一将数字放在末尾
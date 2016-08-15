# iHexin

unittest
```
self.driver.swipe(start_x=279, start_y=205, end_x=88, end_y=205, duration=500)
```

pytest_POM
```
driver.swipe(start_x=300, start_y=239, end_x=39, end_y=239, duration=500)
```

命名规则
1. 页面:对于有一个新page生成需创建一个新page,优先使用标题栏命名,若标题会改变则根据页面功能进行命名
2. 元素:数字开头的元素统一将数字放在末尾
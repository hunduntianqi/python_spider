"""
    options ==> 用于配置浏览器参数
    以谷歌浏览器为例:
        1. 导入浏览器驱动模块
            from selenium import webdriver
        2. 创建谷歌浏览器Options对象
            options = webdriver.ChromeOptions()
        3. 将参数配置对象作为参数传递到创建的浏览器对象中
            web_object = Chrome(options=opt)
        常用配置属性:
            options.add_argument('--disable-infobars') ==> 禁止策略化
            options.add_argument('--no-sandbox') ==> 解决DevToolsActivePort文件不存在的报错
            options.add_argument('window-size=1920x3000') ==> 指定浏览器分辨率
            options.add_argument('--disable-gpu') ==> 谷歌文档提到需要加上这个属性来规避bug
            options.add_argument('--incognito') ==> 隐身模式（无痕模式）
            options.add_argument('--disable-javascript') ==> 禁用javascript
            options.add_argument('--start-maximized') ==> 最大化运行(全屏窗口), 不设置, 取元素可能会报错
            options.add_argument('--disable-infobars') ==> 禁用浏览器正在被自动化程序控制的提示
            options.add_argument('--hide-scrollbars') ==> 隐藏滚动条, 应对一些特殊页面
            options.add_argument('blink-settings=imagesEnabled=false' ==> 不加载图片, 提升速度
            options.add_argument('--headless') ==> 无头浏览器, 浏览器在后台运行, 不显示可视化窗口
            options.binary_location = path ==> 手动指定使用的浏览器位置, 安装浏览器如果不是默认位置, 程序无法找到
                                                浏览器, 需要手动设置安装浏览器路径
"""

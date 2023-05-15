"""
    键盘事件 ==> Keys类:
        selenium通过 Keys 类进行浏览器中的键盘事件操作
        导入类:
            from selenium.webdriver.common.keys import Keys
        常用键盘操作:
            send_keys(Keys.BACK_SPACE): 删除键(BackSpace)
            send_keys(Keys.SPACE): 空格键(Space)
            send_keys(Keys.TAB): 制表键(Tab)
            send_keys(Keys.ESCAPE): 回退键(Esc)
            send_keys(Keys.ENTER): 回车键(Enter)
            send_keys(Keys.CONTROL, 'a'): 全选(Ctrl + A)
            send_keys(Keys.CONTROL, 'c'): 复制(Ctrl + C)
            send_keys(Keys.CONTROL, 'x'): 剪切(Ctrl + X)
            send_keys(Keys.CONTROL, 'v'): 粘贴(Ctrl + V)
            send_keys(Keys.F1): 键盘F1
            .....
            send_keys(Keys.F1): 键盘F12
"""
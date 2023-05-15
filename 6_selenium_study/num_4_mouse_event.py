"""
    鼠标事件 ==> ActionChains类:
        selenium通过 ActionChains 类进行浏览器中的鼠标事件操作
        导入类:
            from selenium.webdriver import ActionChains
        调用ActionChains类, 浏览器驱动作为参数传入:
            ActionChains(web_object)
            ActionChains(web_object).鼠标事件方法.perform()
            perform()为对整个操作的提交动作
        常用方法:
            1. perform(): 执行所有ActionChains中存储的行为
            2. context_click(): 右击
                a. 定位元素:
                    right_click = web_object.find_element('id', 'id_value')
                b. 执行右击操作
                    ActionChains(web_object).context_click(right_click).perform()
            3. double_click(): 双击
                a. 定位元素:
                    double_click = web_object.find_element('id', 'id_value')
                b. 执行双击操作
                    ActionChains(web_object).double_click(double_click).perform()
            4. drag_and_drop(source, target): 拖动源元素到目标元素上释放
                source: 鼠标拖动的源元素
                target: 鼠标释放的目标元素
                a. 定位元素的原位置
                    source = web_object.find_element('id', 'id_value')
                b. 定位元素要拖动到的目标位置
                    target = web_object.find_element('id', 'id_value')
                c. 执行操作
                    ActionChains(web_object).drag_and_drop(source, target).perform()
            5. move_to_element(): 鼠标悬停
                a. 定位元素
                    above = web_object.find_element('id', 'id_value')
                b. 执行操作
                    ActionChains(web_object).move_to_element(above).perform()
            6. move_to_element_with_offset(to_element, xoffset):
                移动到距离某个节点多少距离的位置
            7. move_by_offset(xoffset, yoffset):
                鼠标从当前位置, 移动多少的距离
"""

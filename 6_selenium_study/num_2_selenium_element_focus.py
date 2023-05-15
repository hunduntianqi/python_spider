"""
    元素聚焦:
        当页面上的元素超过一屏后, 想操作屏幕下方的元素, 是不能直接定位到的, 会报元素不可见的
        这种情况下, 正常是需要人借助滚动条来拖动屏幕, selenium里面没有直接的方法去控制滚动条
        需要借助js实现, selenium中的 execute_script() 方法, 可以直接执行js的脚本, 操作js
        1. 实现元素聚焦 ==> 让页面直接跳到元素出现位置:
            target = web_object.find_element_by_xxxx() ==> 定位元素
            web_object.execute_script("arguments[0].scrollIntoView();", target) ==> 执行js实现元素聚焦
        2. 操作竖向滚动条:
            a. 滚动条回到顶部:
                js="var q=document.getElementById('id').scrollTop=0"
                web_object.execute_script(js)
            b. 滚动条拉到底部
                js="var q=document.documentElement.scrollTop=10000"
                web_object.execute_script(js)
                可以修改scrollTop 的值, 来定位右侧滚动条的位置, 0是最上面, 10000是最底部
                以上方法在Firefox和IE浏览器上上是可以的, 但是用Chrome浏览器, 发现不管用
                Chrome浏览器解决办法:
                    js = "var q=document.body.scrollTop=0"
                    web_object.execute_script(js)
        3. 操作横向滚动条:
            有时候浏览器页面需要左右滚动(一般屏幕最大化后, 左右滚动的情况已经很少见了)
            通过坐标控制横向和纵向滚动条 scrollTo(x, y)
            x ==> 横向滚动条横坐标
            y ==> 竖向滚动条纵坐标
            操作代码:
                js = "window.scrollTo(x,y);"
                web_object.execute_script(js)
    设置页面元素等待 ==> 页面元素加载:
        1. 显示等待:
            使webdriver等待某个条件成立时继续执行, 否则在达到最大时长时抛出超时异常(TimeOutException)
            WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions):
                driver: 浏览器驱动
                timeout: 最长超时时间, 默认以秒为单位
                poll_frequency: 检测的间隔时间, 默认为0.5s
                ignored_exceptions: 超时后的异常信息, 默认情况下抛NoSuchElementException异常
                WebDriverWait()一般与until()和until_not()方法配合使用:
                    until(method, message=''): 调用该方法提供的驱动程序作为一个参数, 直到返回值为True
                    until_not(method, message=''): 调用该方法提供的驱动程序作为一个参数, 直到返回值为False
                    例: element = WebDriverWait(driver, 5, 0.5).until(
                    except_conditions.presence_of_element_located((By.ID, 'kw')))
        2. 隐式等待:
            通过一定时长等待页面上的元素加载完成, 如果超出了设置的时长元素还没有加载, 抛出NoSuchElementException异常
            implicitly_wait(time)
                time: 设置等待时长, 默认单位为秒
                例: driver.implicitly_wait(10)
                    driver.get(url)
"""

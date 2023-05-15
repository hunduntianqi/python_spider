"""
    selenium处理 HTML5 的视频播放:
        1. 定位video标签位置
            video = web_object.find_element('xpath', 'xpath_value')
        2. 返回播放文件地址
            url = web_object.execute_script('return arguments[0].currentSrc;', video)
            播放视频
                web_object.execute_script('return arguments[0].play();', video)
            暂停视频
                web_object.execute_script('return arguments[0].pause();', video)
            加载视频
                web_object.execute_script('return arguments[0].load();', video)
"""
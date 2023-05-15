"""
    动态加载数据网站特点:
        1. 查看页面源代码无具体数据
        2. 滚动鼠标滑轮或其他动作时数据才会加载
        3. 页面局部刷新
    动态加载数据分析抓取流程:
        1. F12打开控制台, 执行页面动作开始抓取网络数据包
        2. 抓取返回json文件的网络数据包
        4. XHR: 异步加载的网络数据包
        5. General->Request URL: 返回json数据的URL地址
        6. QueryStringParameters(查询参数) - 观察规律
        注意:请求头中如果带有文件压缩命令, 抓取到的数据会是乱码
    json模块:
        动态网站抓取到的数据一般为json格式, 需要使用json模块进行解析
        1. json.loads(参数为json格式的字符串):
            把json格式的字符串转为python数据类型
            html = json.loads(res.text)
        2. json.dump(python, file, ensure_ascii=False):
            把python的数据类型转为json格式的字符串并存入文件
            参数1: python类型的数据(字典, 列表等)
            参数2: 文件对象
            参数3: ensure_ascii=False序列化时编码
        3. json.dumps(python数据类型):
            把python数据类型转为json格式的字符串
        4. json.load(json格式的字符串):
            将json文件读取, 并转为python类型
"""
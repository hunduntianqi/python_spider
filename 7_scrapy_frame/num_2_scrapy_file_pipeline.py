"""
    Scrapy图片管道:
        Scrapy抓取图片原理:
            利用scrapy提供的图片管道类:from scrapy.pipelines.images import ImagesPipeline
            实现步骤:
                1. 爬虫文件中获取图片链接yield到管道
                2. 管道文件中定义管道继承ImagesPipeline类
                3. 重写类中方法:
                    3.1 get_media_requests(self, item, info)方法:
                        将图片链接交给调度器入队列:yield scrapy.Request(url=item['pic_link'])
                        scrapy会自动下载图片并保存本地
                    3.2 file_path(self, request, response=None, info=None, *, item=None)方法:
                        处理文件路径与文件名
                4. 在settings.py文件中指定图片存储路径
                    IMAGES_STORE = '文件存储路径'(可以自动创建)
            注意:图片下载处理必须安装Pillow模块, 否则程序运行不出错, 但不会成功下载图片, 在日志信息中有如下提示:
                WARNING: Disabled Bian4KMeinvPipeline: ImagesPipeline requires installing Pillow 4.0.0 or later
                在ImagesPipeline管道类中不要在最上面定义其他方法, 一旦有方法Return item, 也会导致图片无法下载！！！
    Scrapy文件管道:
        Scrapy抓取文件原理:
            利用scrapy提供的文件管道类:from scrapy.pipelines.files import FilesPipeline
            实现步骤:
                1. 爬虫文件中获取文件链接yield到管道
                2. 管道文件中定义管道继承FilesPipeline类
                3. 重写类中方法:
                    3.1 get_media_requests(self, item, info)方法:
                        将文件链接交给调度器入队列:yield scrapy.Request(url=item['file_link'])
                        scrapy会自动下载文件并保存本地
                    3.2 file_path(self, request, response=None, info=None, *, item=None)方法:
                        处理文件路径与文件名
                4. 在settings.py文件中指定文件存储路径
                    FILES_STORE = '文件存储路径'(可以自动创建)

    Scrapy视频管道:
        Scrapy抓取视频原理:
            利用scrapy提供的视频管道类:from scrapy.pipelines.media import MediaPipeline
            实现步骤:
                1. 爬虫文件中获取视频链接yield到管道
                2. 管道文件中定义管道继承MediaPipeline类
                3. 重写类中方法:
                    3.1 get_media_requests(self, item, info)方法:
                        将文件链接交给调度器入队列:yield scrapy.Request(url=item['media_link'])
                        scrapy会自动下载文件并保存本地
                    3.2 file_path(self, request, response=None, info=None, *, item=None)方法:
                        处理文件路径与文件名
                4. 在settings.py文件中指定文件存储路径
                    MEDIAS_STORE = '文件存储路径'(可以自动创建)
"""
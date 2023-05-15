# Scrapy settings for BiAn4K_MeiNv project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent

BOT_NAME = 'BiAn4K_MeiNv'

SPIDER_MODULES = ['BiAn4K_MeiNv.spiders']
NEWSPIDER_MODULE = 'BiAn4K_MeiNv.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 配置UA参数
# USER_AGENT = str(UserAgent().random)

# Obey robots.txt rules
# 不遵守robots协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 设置最大并发量为4
# CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置下载延迟时间为1s
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 设置请求头信息
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'referer': 'https://pic.netbian.com/4kmeinv/',
    'cookie': '__yjs_duid=1_50cc160f44fa1889109b49298067095a1643466557484; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1643466550; zkhanecookieclassrecord=%2C54%2C65%2C; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1643466943',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': str(UserAgent().random)
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'BiAn4K_MeiNv.middlewares.Bian4KMeinvSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'BiAn4K_MeiNv.middlewares.Bian4KMeinvDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 开启管道文件
ITEM_PIPELINES = {
    # 'BiAn4K_MeiNv.pipelines.MkDir': 1,
    'BiAn4K_MeiNv.pipelines.Bian4KMeinvPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
IMAGES_STORE = r'D:\Users\Administrator\IdeaProjects\python_爬虫\2022_1_29_Scrapy框架\Scrapy框架练习\BiAn4K_MeiNv\BiAn4K_MeiNv\images'
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_HOST = "127.0.0.1"
REDIS_PORT= 6379
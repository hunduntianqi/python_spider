'''
    全局配置文件
'''
from fake_useragent import UserAgent

# Scrapy settings for Scrapyexplain project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Scrapyexplain'  # 项目目录名

SPIDER_MODULES = ['Scrapyexplain.spiders']
NEWSPIDER_MODULE = 'Scrapyexplain.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
"""设置USER-AGENT"""
USER_AGENT = str(UserAgent().random)

# Obey robots.txt rules
"""是否遵循robots协议, True为遵守, False为不遵守"""
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
"""最大并发量, 默认为16, 加快数据抓取频率的操作"""
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
"""下载延迟时间, 指每隔一定时间发送一次请求, 降低数据抓取频率的操作"""
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
"""是否启用cookies, 默认禁用, 取消注释代表开启cookies, 与True/False无关"""
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
"""禁用Telnet控制台(默认是启用)"""
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
"""请求头, 类似于requests.get()方法中的headers参数, uesr-agent也可以在此处设置"""
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
    'cookie': 'uuid=a4f16cd9-88c6-4272-f612-9d88b1ba6f26; sessionid=ed25f423-a127-4153-f3e2-b18acfed8a33; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; cityDomain=zz; puuid=ddab02c1-073e-4390-c77b-762b87b59473; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%22a4f16cd9-88c6-4272-f612-9d88b1ba6f26%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%222%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22sessionid%22%3A%22ed25f423-a127-4153-f3e2-b18acfed8a33%22%7D; user_city_id=103',
    'referer': 'https://m.guazi.com/'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
"""启用或禁用爬虫中间件, 543是优先级, 数字越小, 优先级越高(优先被使用)"""
# SPIDER_MIDDLEWARES = {
#    'Scrapyexplain.middlewares.ScrapyexplainSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
"""启用或禁用下载器中间件, 543是优先级, 数字越小, 优先级越高(优先被使用)"""
# DOWNLOADER_MIDDLEWARES = {
#    'Scrapyexplain.middlewares.ScrapyexplainDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
"""启用或禁用扩展程序"""
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
""" 
配置项目管道(管道文件中可以定义多个管道类, 根据优先级不同先后执行)
  项目目录名.模块名.类名:优先级(1-1000之间, 数字越小, 优先级越高)
"""
ITEM_PIPELINES = {
    'Scrapyexplain.pipelines.ScrapyexplainPipeline': 300,
    # 'Scrapyexplain.pipelines.ScrapyexplainPipeline2': 200,
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
# HTTPCACHE_STORAGE = 'scrapy.extension

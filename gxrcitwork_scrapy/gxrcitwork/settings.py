# -*- coding: utf-8 -*-

# Scrapy settings for gxrcitwork project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
# import time


BOT_NAME = 'gxrcitwork'

SPIDER_MODULES = ['gxrcitwork.spiders']
NEWSPIDER_MODULE = 'gxrcitwork.spiders'
RANDOM_UA_TY = 'RANDOM'
# 加载下载中间件的路径，随机请求头之类的
DOWNLOADER_MIDDLEWARES = {
   # 'five_eight_Jobcity.middlewares.FiveEightJobcityDownloaderMiddleware': 543,
   # 使用自定义的IP代理
   'gxrcitwork.Mid.IPProxy.ProxyMiddleware': 125,
   'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 128,
   # 启用自定义useragent函数
   # 'gxrcitwork.Mid.random_ua.RandomUserAgentMiddleware': 543,
   # 禁用系统自带的useragent函数
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
}
# 储存用的管道文件加载路径
ITEM_PIPELINES = {
    'gxrcitwork.pipelines.GxrcitworkPipeline': 300,
}
# 设置下载延迟单位是秒，可以用random函数设定随机值
DOWNLOAD_DELAY = random.randint(2,4)
# 设置网页响应延迟，单位: 秒
DOWNLOAD_TIMEOUT = 180
# 降低log日志记录的级别
LOG_LEVEL = 'INFO'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发请求 默认:16
CONCURRENT_REQUESTS = 128

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gxrcitwork (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gxrcitwork.middlewares.GxrcitworkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'gxrcitwork.middlewares.GxrcitworkDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'gxrcitwork.pipelines.GxrcitworkPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

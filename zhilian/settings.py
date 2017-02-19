# -*- coding: utf-8 -*-

# Scrapy settings for zhilian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'zhilian'

SPIDER_MODULES = ['zhilian.spiders']
NEWSPIDER_MODULE = 'zhilian.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhilian (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/49.0.2623.87 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
  'Accept-Encoding': 'gzip, deflate, sdch',
  'Connection': 'keep-alive',
  '':'',
  'cookie':'accessID=20161222215102844; Hm_lvt_5497f3e5cf06014777f01fb0307e58f4=1482414663; tempID=6388780048; __auc=2aa6c7eb15926cd6b5d52dd27c8; hnqxMark=1; userapp_promoteletter_status142964501=1; userapp_shangwufc6_status142964501=1; cookie_pcc=1%7C%7Cbaidu%7C%7C313012-00003%7C%7Chttps%3A//www.baidu.com/baidu.php%3Fsc.af0000jT6JN_mhQrXFG-Yr4NvQFpeGkQ9EBw7aiSX2mswEpyFGXfdT9IC7I8K0_i_yT01q2OWU_wpqumjChP77ua435Jd-3PcVQkiggEe0u0wXB6E9COhb2JRPJ8Ef1iAOtzd6zwDPNwdi4fAdXAC2OYanSzkfEOer-nIGgdvLI8NMQNuf.7D_aq-qiRfgGCnYDkYcQYYApamlZQDM6C_kgmvIiXxxAlBSZfkgdSAGh2FP7BqM76lOal4QZAEWugb1vyyyTNBmLeSMFg__zTVHQ8gZJyAp7WGePdhqf.U1Yk0ZDq_Phl1sKY5Uju8_t0pyYqnWcd0ATqIyNsT1D0Iybqmh7GuZN_UfKspyfqn6KWpyfqPj0z0AdY5Hnkn1uxnH0kPdtknjD1g1Dsn17xn1msnfKopHYs0ZFY5HndPsK-pyfqnHf1n-tznH6zndtznHDkPNtznH6sn-tznHRdnsKBpHYznjf0Uynqn7tzrH0krH6vrjFxnHcsrHT1nWRkg1c4njmLrHf1nNts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0KEIhsqnHckQHNxnW0LHaYknjNxnWmvridbX-tzPWm4yadbX-tzP1TYQywlg1fdrjnVn-tYrj6sQH7xPH0vriYkg1R1PadbX-tdPWRLQHFxPHmvPiYkg1RLPjmVuZGxPHTLPzYkg1R4n1TVn7tvnHTLQH7xPWcYradbX-tvnWTLQHDvg1m1rHTVuZGxPWfYPidbX-tvPjmvQywlg1mdnjfVuZGxPWRkPBdbX-tvPHfzQywlg1mdPWDVnNtvPHm1QHFxPWR3nzYkg1mdrjmVuZGxPWR4raYkP7tvPWckQywlg1mvnWcVuZC0mycqn7ts0ANzu1Ys0ZKs5HTsPjmzPjnLnfK8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0IZN15HDvn16vPWnYP163PHf1n1fYnW6k0ZF-TgfqnHf3nWmYnj0YPWfsP6K1pyfquhcYuWbkPhmsnj0dPynkP0KWTvYqfW0dnDfkwH7aPDn4nYPDnsK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0KbIA-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KlTAkdT1Ys0A7buhk9u1Yk0APzm1YYnWfYn0%26ck%3D6327.10.62.326.141.213.137.1429%26shh%3Dwww.baidu.com%26sht%3D99621802_hao_pg%26us%3D1.0.1.0.0.0.0.0%26ie%3Dutf-8%26f%3D8%26srcqid%3D526996916608339756%26tn%3D99621802_hao_pg%26wd%3D%25E7%2599%25BE%25E5%2590%2588%26oq%3D%25E7%2599%25BE%25E5%2590%2588%26rqlang%3Dcn%26sc%3DUWY4rHmznH6sn-qCmyqxTAThIjYkPj6zPWfsnjnvnjc3FhnqpA7EnHc1Fh7W5HfkP1RdPjf3rHT%26ssl_sample%3Ds_4%252Cs_8%252Cs_12%26bc%3D110101; userapp_shangwufc5_status142964501=1; accessToken=BH148264203538027092; lastLoginDate=2016-12-25+13%3A01%3A22; _fmdata=E71634353A5EFF38AF8BA113D6ADEF9E28F748D9E6C1081614C8FECC840FB604E60B8EA952BC39BB8CC6167C1740C37B33FE3F20C04E4427; channel=baidu; code=313012-00003; AuthCookie=4BFFD62B611D896EBA693B4B353FEAC52386D6DA65478749DAB637FB03F3A62F08F8C44E3F82267F904AF051C2A81FF4D7A6E2425F8EA858DA120F35652A8CB639E76A1BD4F820C26BFB0F813A653583; GCUserID=142964501; OnceLoginWEB=142964501; LoginEmail=18119500180%40mobile.baihe.com; userID=142964501; spmUserID=142964501; AuthCheckStatusCookie=CBAD37840873EF66310D0A60B87D666B14D1D3015978705726A127B203C4931405E9D878DCC812E7; Hm_lvt_5caa30e0c191a1c525d4a6487bf45a9d=1482638512,1482638972,1482640056,1482642036; Hm_lpvt_5caa30e0c191a1c525d4a6487bf45a9d=1482642390; nTalk_CACHE_DATA={uid:kf_9847_ISME9754_142964501}; NTKF_T2D_CLIENTID=guestTEMPEE25-8992-856D-7702-26CD272B26B7'
}
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhilian.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhilian.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhilian.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.curdir))

MONGO_URI = 'mongodb://localhost:27017'

ITEM_PIPELINES = {
    'zhilian.pipelines.ZhilianPipeline': 500,
}

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
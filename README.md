# GxTalentNetwork_Crawl
广西人才网职位爬取

## 前言
&nbsp;&nbsp;&nbsp;&nbsp;- 这个项目有两个版本，一个是我用scrapy框架做的，在去年即18年的5月份，另外一个是单使用多线程制作。</br>
&nbsp;&nbsp;&nbsp;&nbsp;- scrapy版本由于是去年制作的，当时人才网还没改版，现在改版后可能失效，这个有时间我会用scrapy重构一次。</br>
&nbsp;&nbsp;&nbsp;&nbsp;- 多线程版本是近期制作的，如果无法运行，应该是因为本地ip池的原因，将ip池模块删除，或者使用自己的ip池模块替代也可。
  
## scrapy版本
下面是项目目录

 - gxrcitwork
     - gxrcitwork
         - IPPool
         - Mid
             - IPProxy.py
         - spiders
             - myspider.py 
         - `__init__.py`
         - items.py
         - middlewares.py
         - pipelines.py
         - settings.py
     - scrapy.cfg
     - scrapy_start.py 	

```
IPPool: 来自GitHub大神的项目代理池
Mid: 自定义中间件，用来存放处理处理ip池代码
spiders: 爬虫程序主体，负责处理response，解析，将需要跟进的url提交给爬虫引擎
items.py: 用于处理文件，除杂
middlewares.py: 系统中间件
pipelines.py: 管道文件，负责处理爬虫获得的数据，存入数据库
settings: 配置文件
```
如果需要对接代理池项目：

 - 请在Mid文件夹下添加代码
 - 修改settings配置文件中的`gxrcitwork.Mid.IPProxy.ProxyMiddleware`中ProxyMiddleware为ip项目文件名即可

 练手之作，代码简陋，XD，大神轻喷
 
## 多线程版本
### 文件目录

 - api
    - proxy.py
 - db
    - Get_DB.py
    - KeepDB.py
    - PoolDB.py
 - test
 - util
    - jedge.py
    - requests_url.py
 - config.py
 - main_v0.1.py    

```
api: 存放ip池调度文件
db: 存放mysql数据库存储读取文件
test: 测试用文件夹
util: 存放通用函数文件夹
config.py: 存放配置文件
main_v0.1.py: 运行主程序
```
## 使用方法

 1、scrapy版本
 	直接运行目录下，scrapy_start.py文件即可
 	
 2、多线程版本
 	运行目录下main_v0.1.py版本
 	
 **注：如有报错，请仔细查看缺少哪些包，上 https://pypi.org/ 搜索下载，使用python3 install 即可**
练手之作，代码简陋，XD，大神轻喷

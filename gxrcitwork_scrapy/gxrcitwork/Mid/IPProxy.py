import random
import requests
import json
from gxrcitwork.IPPool import Util
# from tencent.settings import IPPOOL


class ProxyMiddleware(object):
    '''
    设置Proxy
    '''
    def __init__(self):
        # self.ip = ip
        pass

    def process_request(self, request, spider):
        proxy = self.get_proxy()
        print("添加代理中")
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        if request.status != 200:
            proxy = self.get_proxy()
            print("代理失效，重新获取代码")
            request.meta['proxy'] = proxy
            return request

        return response

    def get_proxy(self):
        # items = {}
        # protocol = random.randint(0,1)
        items = {}
        response = requests.get("http://127.0.0.1:8000/?types=0&count=1&protocol=0").text
        protocol_list = json.loads(response)
        for i in protocol_list:
            items["ip"] = i[0]
            items["port"] = i[1]
        proxy = "http://" + str(items["ip"]) + ":" + str(items["port"])
        return proxy
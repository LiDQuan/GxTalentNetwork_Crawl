from random import choice
from re import findall
from threading import Thread

from requests import get

import gxrcitwork.IPPool.Config
import gxrcitwork.IPPool.ProxiesDataBase

d = {}
ip_list = []


def GetPageContent(tar_url):
    url_content = ""
    try:
        url_content = get(tar_url,
                          headers={
                              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                              'Accept-Encoding': 'gzip, deflate, compress',
                              'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
                              'Cache-Control': 'no-cache',
                              'Connection': 'keep-alive',
                              'Upgrade-Insecure-Requests': "1",
                              'User-Agent': choice(gxrcitwork.IPPool.Config.UserAgents)
                          }).text
    except BaseException as e:
        pass
    finally:
        return url_content


def GetIP():
    global d
    global ip_list
    thread_list = []
    ips = []

    for tar_url in gxrcitwork.IPPool.Config.Url_Regular.keys():
        url_content = GetPageContent(tar_url)
        regular = gxrcitwork.IPPool.Config.Url_Regular.get(tar_url, "")
        tmp_ip_list = findall(regular, url_content)
        for item in tmp_ip_list:
            ip_list.append("{}:{}".format(item[0], item[1]))

    for index in range(0, gxrcitwork.IPPool.Config.MaxThreads):
        thread_list.append(Thread(target=VerifyIp))
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()

    for item in d.keys():
        ips.append(item)
    d.clear()
    gxrcitwork.IPPool.ProxiesDataBase.AddItems(ips)


def RefreshDB():
    global d
    global ip_list
    ip_list = ProxiesDataBase.GetItems()
    thread_list = []
    ips = []

    if len(ip_list) < 1:
        return


    for index in range(0, Config.MaxThreads):
        thread_list.append(Thread(target=VerifyIp))
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()

    gxrcitwork.IPPool.ProxiesDataBase.ClearItems()

    for item in d.keys():
        ips.append(item)
    d.clear()
    gxrcitwork.IPPool.ProxiesDataBase.AddItems(ips)


def VerifyIp():
    global d
    while ip_list:
        tmp_ip_port = ip_list.pop(0)
        print("verify ip: {}".format(tmp_ip_port))
        proxies = {"http": "http://{}".format(tmp_ip_port), "https": "https://{}".format(tmp_ip_port)}
        try:
            url_content = get(gxrcitwork.IPPool.Config.TestUrl,
                              proxies=proxies,
                              timeout=gxrcitwork.IPPool.Config.TestTimeOut,
                              headers={
                                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                  'Accept-Encoding': 'gzip, deflate, compress',
                                  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
                                  'Cache-Control': 'max-age=0',
                                  'Connection': 'keep-alive',
                                  'User-Agent': choice(gxrcitwork.IPPool.Config.UserAgents)
                              })

            if int(url_content.status_code) == int(200):
                d.update({"{}".format(tmp_ip_port): 0})
        except BaseException as e:
            continue

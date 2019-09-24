# -*- coding: utf-8 -*-
import scrapy
import time
import random
from gxrcitwork.IPPool import Util
from gxrcitwork.items import GxrcitworkItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['www.gxrc.com']
    # page = 1
    # url = 'http://s.gxrc.com/sJob?schType=1&District=2&Industry=2473%2C2477%2C2474%2C2475%2C2471&page='
    # 更新ip池
    # Util.Refresh()
    start_urls = []
    for pn in range(1,5):
        # url = 'http://s.gxrc.com/sJob?schType=1&District=2&Industry=2473%2C2477%2C2474%2C2475%2C2471&page=' + str(pn)
        url = 'http://s.gxrc.com/sJob?schType=1&district=2&industry=2473%2C2477%2C2474%2C2475%2C2471&pageSize=20&orderType=0&listValue=1&keyword=%E8%AE%BE%E8%AE%A1&page='+ str(pn)
        print(url)
        start_urls.append(url)
    # 获取每页的岗位岗位链接
    def parse(self, response):

        # for links in response.xpath("//div[@class='rlOne']"):
        link = response.xpath("//div[@class='rlOne']/ul/li/h3/a/@href").extract()
        # print(link)
        for temp in link:
            time.sleep(random.randint(1,3))
            yield scrapy.Request(temp, callback = self.link_parse)

    # 获取每页岗位详细信息
    def link_parse(self, response):
        print("进入二级页面解析")
        for temp in response.xpath("//div[@class='gsR_con']"):
            item = GxrcitworkItem()
            # 岗位名名 positionName
            item["positionName"] = temp.xpath(".//h1[@id='positionName']/text()").extract()[0]
            item["positionName"] = item['positionName'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 招聘企业 company
            item["company"] = temp.xpath("./div[@class='gsR_con_top']/div/a/text()").extract()[0]
            item["company"] = item['company'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 招聘人数 hiring
            item["hiring"] = temp.xpath(".//table[@class='gs_zp_table']//tr[1]/td[1]/text()").extract()[0]
            item["hiring"] = item['hiring'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 学历 education
            item["education"] = temp.xpath(".//table[@class='gs_zp_table']//tr[1]/td[2]/text()").extract()[0]
            item["education"] = item['education'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 薪资待遇 salary
            item["salary"] = temp.xpath(".//table[@class='gs_zp_table']//tr[2]/td[1]/text()").extract()[0]
            item["salary"] = item['salary'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 工作年限 work_year
            item["work_year"] = temp.xpath(".//table[@class='gs_zp_table']//tr[2]/td[2]/text()").extract()[0]
            item["work_year"] = item['work_year'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 工作地点 word_site
            item["word_site"] = temp.xpath(".//table[@class='gs_zp_table']//tr[3]/td[1]/text()").extract()[0]
            item["word_site"] = item['word_site'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 工作性质 work_nature
            item["work_nature"] = temp.xpath(".//table[@class='gs_zp_table']//tr[3]/td[2]/text()").extract()[0]
            item["work_nature"] = item['work_nature'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 工作身高 work_height
            item["work_height"] = temp.xpath(".//table[@class='gs_zp_table']//tr[4]/td[2]/text()").extract()[0]
            item["work_height"] = item['work_height'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 工作年龄 work_age
            item["work_age"] = temp.xpath(".//table[@class='gs_zp_table']//tr[5]/td[1]/text()").extract()[0]
            item["work_age"] = item['work_age'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 工作性别 work_sex
            item["work_sex"] = temp.xpath(".//table[@class='gs_zp_table']//tr[6]/td[1]/text()").extract()[0]
            item["work_sex"] = item['work_sex'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 语言/程度 work_language
            item["work_language"] = temp.xpath(".//table[@class='gs_zp_table']//tr[7]/td[1]/text()").extract()[0]
            item["work_language"] = item['work_language'].replace("\r","").replace("\n","").replace(" ","").replace("\xa0","")  # 去除多余字符
            # 招聘发布时间 work_time
            item["work_time"] = temp.xpath(".//table[@class='gs_zp_table']//tr[7]/td[2]/text()").extract()[0]
            item["work_time"] = item['work_time'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 公司福利 work_welfare
            item["work_welfare"] = temp.xpath(".//table[@class='gs_zp_table']//tr[7]/td/text()").extract()[0]
            item["work_welfare"] = item['work_welfare'].replace("\r","").replace("\n","").replace(" ","").replace("\xa0","") # 去除多余字符
            # 工作内容及要求 examineSensitiveWordsContent
            item["examineSensitiveWordsContent"] = temp.xpath(".//p[@id='examineSensitiveWordsContent']/text()").extract()
            # item["examineSensitiveWordsContent"] = item['examineSensitiveWordsContent'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 联系人 linkman
            item["linkman"] = temp.xpath(".//table[@class='address']//tr[2]/td/text()").extract()[0]
            item["linkman"] = item['linkman'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 电子邮件 company_email
            item["company_email"] = temp.xpath(".//table[@class='address']//tr[3]/td/text()").extract()[0]
            item["company_email"] = item['company_email'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 企业官网 company_net
            item["company_net"] = temp.xpath(".//table[@class='gs_zp_table']//tr[4]/td/text()").extract()[0]
            item["company_net"] = item['company_net'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 联系地址 company_address
            item["company_address"] = temp.xpath(".//table[@class='address']//tr[5]/td/text()").extract()[0]
            item["company_address"] = item['company_address'].replace("\r","").replace("\n","").replace(" ","") # 去除多余字符
            # 招聘企业	linkList
            item["linkList"] = temp.xpath("./div[@class='gsR_con_top']/div/a/@href").extract()[0]
            yield item


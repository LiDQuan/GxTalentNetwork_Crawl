# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 主要用于文件的处理，去空格/去换行、提取数字、加密等等功能
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst,MapCompose,Join

# 去换行\空格
# 用法，在Field()函数中，添加 input_processor=MapCompose(do_strip)
def do_strip(value):
    return value.strip()

class GxrcitworkItem(scrapy.Item):
    # define the fields for your item here like:
    # 岗位名名 positionName
    positionName = scrapy.Field()
    # 招聘企业 company
    company = scrapy.Field()
    # 招聘人数 hiring
    hiring = scrapy.Field()
    # 学历 education
    education = scrapy.Field()
    # 薪资待遇 salary
    salary = scrapy.Field()
    # 工作年限 work_year
    work_year = scrapy.Field()
    # 工作地点 word_site
    word_site = scrapy.Field()
    # 工作性质 work_nature
    work_nature = scrapy.Field()
    # 工作身高 work_height
    work_height = scrapy.Field()
    # 工作年龄 work_age
    work_age = scrapy.Field()
    # 工作性别 work_sex
    work_sex = scrapy.Field()
    # 语言/程度 work_language
    work_language = scrapy.Field()
    # 招聘发布时间 work_time
    work_time = scrapy.Field()
    # 公司福利 work_welfare
    work_welfare = scrapy.Field()
    # 工作内容及要求 examineSensitiveWordsContent
    examineSensitiveWordsContent = scrapy.Field()
    # 联系人 linkman
    linkman = scrapy.Field()
    # 电子邮件 company_email
    company_email = scrapy.Field()
    # 企业官网 company_net
    company_net = scrapy.Field()
    # 联系地址 company_address
    company_address = scrapy.Field()
    # 招聘企业	linkList
    linkList = scrapy.Field()




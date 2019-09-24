# -*- coding: utf-8 -*-

# Define your item pipelines here
# 管道文件，主要用于储存文件
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

class GxrcitworkPipeline(object):
    # 当爬虫运行时，该方法会被调用
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            db='python4',
            user='root',
            passwd='123456',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        # self.filename = open("gxrcw.json","w")

    # 必须返回一个数据字典或者item对象
    def process_item(self, item, spider):
        text = dict(item)
        self.cursor.execute("""
        INSERT IGNORE INTO gxrcJob(positionName, company, hiring, education, salary, work_year, word_site, work_nature, work_height, work_age, work_sex, work_language, work_time, work_welfare, examineSensitiveWordsContent, linkman, company_email, company_net, company_address, linkList
)VALUE("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")
        """%(
            text['positionName'],
            text['company'],
            text['hiring'],
            text['education'],
            text['salary'],
            text['work_year'],
            text['word_site'],
            text['work_nature'],
            text['work_height'],
            text['work_age'],
            text['work_sex'],
            text['work_language'],
            text['work_time'],
            text['work_welfare'],
            text['examineSensitiveWordsContent'],
            text['linkman'],
            text['company_email'],
            text['company_net'],
            text['company_address'],
            text['linkList']
        ))
        self.conn.commit()
        # text = json.dumps(dict(item), ensure_ascii = False)
        # self.filename.write(text)
        # for temp in text:
            # self.filename.write(temp['name'])
        print("正在进行数据插入")
        return item

    # 当爬虫关闭时，这个方法被调用
    def close_spider(self, spider):
        # self.filename.close()
        self.conn.close()
        print("完成数据插入。")

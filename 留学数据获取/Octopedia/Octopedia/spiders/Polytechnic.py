#coding:utf-8
import scrapy
import csv
import os
class CMU_Spider(scrapy.Spider):
    name="Polytechnic"
    start_urls = ["https://www.niche.com/k12/polytechnic-school-pasadena-ca/"]
    def parse(self, response):
        Cost = response.xpath(".//div[@class='scalar__bucket']")
        CostLabel = Cost.xpath(".//div[@class='scalar__label']/span/text()").extract_first()
        CostValue = "School" + Cost.xpath(".//div[@class='scalar__value']/span/text()").extract_first()
        print(CostLabel + " " + CostValue)
        messages = response.xpath(".//div[@class='blank__bucket']")
        Address=messages.xpath(".//div[@class='profile__address']")
        info=Address.xpath('string(.)').extract()[0]
        address_lable=info[0:7]
        address_value=info[7:]
        print(address_lable+" "+address_value)
        # print(address_label+"  "+address_value)
        Majors = messages.xpath(".//ul[@class='popular-entities-list']/li[@class='popular-entities-list-item']")
        print("Hello world\nMost Popular Majors: ")
        print(os.path.basename(__file__).split(".")[0] + ".csv")
        filename = os.path.basename(__file__).split(".")[0] + ".csv"
        if (os.path.exists(filename) == False):
            open(filename, "w")
        csvFile = open(filename, "r+", encoding="utf-8")
        try:
            writer = csv.writer(csvFile)
            writer.writerow(("key", "value"))
            writer.writerow((CostLabel, CostValue))
            writer.writerow((address_lable,address_value))
            for message in messages:
                labels=message.xpath(".//div[@class='scalar__label']")
                values=message.xpath(".//div[@class='scalar__value']")
                for i in range(len(labels)):
                    label=str(labels[i].xpath(".//span/text()").extract_first())
                    value=str(values[i].xpath(".//span/text()").extract_first())
                    if label and value is not None:
                        writer.writerow((label,value))
        except:
            print("lables or values is error")

        print("++++++++++++++++++++++++")

        try:
            writer.writerow(("major", "graduates"))
            for majors in Majors:
                major=majors.xpath(".//h6[@class='popular-entity__name']/text()").extract_first()
                graduates=majors.xpath(".//div[@class='popular-entity-descriptor']/text()").extract_first()
                if major and graduates is not None:
                    print(major)
                    print(graduates)
                    writer.writerow((major,graduates))
        except:
            print("major has errors")
        finally:
            csvFile.close()
        print("Hello world")


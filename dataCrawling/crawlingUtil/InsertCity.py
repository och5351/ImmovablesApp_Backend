# -*- coding: utf-8 -*-
from crawlingUtil.CityUtilCrawling import CityUtilCrawling
from crawlingUtil.Selenium import Selenium
import re
import time
import winsound as ws
from DataBase.DBConnector import DBConnector

class InsertCity:

    city = ''
    cityCode = ''
    contry = ''
    town = ''
    se = Selenium()
    crawlingUtil = CityUtilCrawling()
    cityName = ''
    contryName = ''
    openButton = ''
    cityButton = ''
    contryButton = ''
    townButton = ''
    db = None
    contryStartP = 26
    townStartP = 468
    tempTownNum = 0
    code = 0

    def __init__(self, url):
        self.db = DBConnector()
        self.se.startSelenium(url)
        self.findCity()
        self.db.conn.commit()
        self.db.DBCloser()

    def findCity(self):

        self.openButton = '//*[@id="region_filter"]/div/a/span[1]'
        self.se.buttonClick(self.openButton)

        tempCityArr = []  # 임시 리스트
        tempCityArr.append(self.se.driver.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[2]/ul').text)
        tempCityArr[0] = tempCityArr[0].replace('\n', ',')
        tempCityArr = tempCityArr[0].split(',')
        # print(tempCityArr)
        cNum = len(tempCityArr)
        time.sleep(1)

        for click in range(cNum): #시 버튼 클릭
            if click > 0:
                try:
                    self.city = tempCityArr[click]
                    self.cityButton = '//*[@id="region_filter"]/div/div/div[2]/ul/li['+str(click+1)+']'
                    self.se.buttonClick(self.cityButton)
                    time.sleep(2)

                    self.cityCode = self.db.selectCity(self.city)

                    self.findContry()
                    time.sleep(2)
                    cityOpenButton = '//*[@id="region_filter"]/div/a/span[1]'
                    self.se.buttonClick(cityOpenButton)
                    time.sleep(2)
                    self.se.buttonClick(cityOpenButton)
                    time.sleep(1)


                except:
                    None

    def findContry(self):

        tempContryArr = []  # 임시 리스트
        tempContryArr.append(self.se.driver.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[2]/ul').text)
        tempContryArr[0] = tempContryArr[0].replace('\n', ',')
        tempContryArr = tempContryArr[0].split(',')
        #self.db.InsertDB(tempContryArr)
        #print(tempContryArr)
        contNum = len(tempContryArr)
        time.sleep(1)

        for click in range(contNum): # 읍/면/구
            try:
                self.contry = tempContryArr[click]
                self.contryButton = '//*[@id="region_filter"]/div/div/div[2]/ul/li['+str(click+1)+']'
                self.se.buttonClick(self.contryButton)
                time.sleep(2)
                self.db.InsertContry(self.contry, self.contryStartP, self.cityCode)
                self.findTown()
                time.sleep(2)
                self.se.buttonClick('//*[@id="region_filter"]/div/a/span[1]')
                time.sleep(1)
                self.se.buttonClick('//*[@id="region_filter"]/div/a/span[1]')
                time.sleep(1)
                self.se.buttonClick(self.cityButton)
                time.sleep(1)
                self.contryStartP += 1
            except:
                None

    def findTown(self):
        tempTownArr = [] #임시 리스트
        tempTownArr.append(self.se.driver.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[2]/ul').text)
        tempTownArr[0] = tempTownArr[0].replace('\n', ',')
        tempTownArr = tempTownArr[0].split(',')

        time.sleep(3)
        townNum = len(tempTownArr)



        for click in range(townNum):
            try:
                self.town = tempTownArr[click]
                #self.townButton = '//*[@id="region_filter"]/div/div/div[2]/ul/li['+str(click + 1)+']'
                #self.se.buttonClick(self.townButton)
                self.db.InsertTown(self.town, self.townStartP, self.contryStartP)
                self.townStartP += 1
            except:
                None

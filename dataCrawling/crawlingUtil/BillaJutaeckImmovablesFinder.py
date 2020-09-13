# -*- coding: utf-8 -*-
from crawlingUtil.CityUtilCrawling import CityUtilCrawling
from crawlingUtil.Selenium import Selenium
import re
import time
import winsound as ws

class BillaJutaeckImmovablesFinder:
    city = ''
    contry = ''
    town = ''
    se = Selenium()
    crawlingUtil = CityUtilCrawling()
    cityName = ''
    contryName = ''
    OUTPUT_FILE_NAME = 'Immovables.txt'
    open_output_file = None
    openButton = ''
    cityButton = ''
    contryButton = ''
    townButton = ''

    def __init__(self, url):
        self.se.startSelenium(url)
        self.findCity()
        self.open_output_file.close()

    def findCity(self):
        JBButton ='//*[@id="wrap"]/div[1]/a[2]'
        self.se.buttonClick(JBButton)


        self.openButton = '//*[@id="region_filter"]/div/a/span[1]'
        self.se.buttonClick(self.openButton)

        tempCityArr = []  # 임시 리스트
        tempCityArr.append(self.se.driver.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[2]/ul').text)
        tempCityArr[0] = tempCityArr[0].replace('\n', ',')
        tempCityArr = tempCityArr[0].split(',')
        # print(tempCityArr)
        cNum = len(tempCityArr)
        time.sleep(1)
        for click in range(cNum):  # 시 버튼 클릭
            try:
                self.OUTPUT_FILE_NAME = tempCityArr[click] + ' ' + 'Immovables.txt'
                self.open_output_file = open(self.OUTPUT_FILE_NAME, 'w', -1, "utf-8")
                self.city = tempCityArr[click]
                self.cityButton = '//*[@id="region_filter"]/div/div/div[2]/ul/li[' + str(click + 1) + ']'
                self.se.buttonClick(self.cityButton)
                time.sleep(2)
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

        # print(tempContryArr)
        contNum = len(tempContryArr)
        time.sleep(1)
        for click in range(contNum):  # 읍/면/구
            if click > 8:
                try:
                    self.contry = tempContryArr[click]
                    self.contryButton = '//*[@id="region_filter"]/div/div/div[2]/ul/li[' + str(click + 1) + ']'
                    self.se.buttonClick(self.contryButton)
                    time.sleep(2)
                    self.findTown()
                    time.sleep(2)
                    self.se.buttonClick('//*[@id="region_filter"]/div/a/span[2]')
                    time.sleep(2)
                    self.se.buttonClick('//*[@id="region_filter"]/div/a/span[2]')
                    time.sleep(1)
                except:
                    None

    def findTown(self):
        tempTownArr = []  # 임시 리스트
        tempTownArr.append(self.se.driver.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[2]/ul').text)
        tempTownArr[0] = tempTownArr[0].replace('\n', ',')
        tempTownArr = tempTownArr[0].split(',')

        # print(tempTownArr)
        townNum = len(tempTownArr)
        time.sleep(1)
        for click in range(townNum):
            try:
                self.town = tempTownArr[click]
                self.townButton = '//*[@id="region_filter"]/div/div/div[2]/ul/li[' + str(click + 1) + ']'
                self.se.buttonClick(self.townButton)
                time.sleep(1)
                self.detailImmovable()
                time.sleep(1)
                self.se.buttonClick('//*[@id="region_filter"]/div/a/span[3]')
                time.sleep(1)
            except:
                None

    def findImmovables(self):
        tempImmovables1 = []
        tempImmovables2 = []
        print(1)
        tempImmovables1.append(self.se.driver.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[3]/ul').text)
        print(tempImmovables1)
        tempImmovables1[0] = tempImmovables1[0].replace('\n', ',')
        tempImmovables1 = tempImmovables1[0].split(',')
        immovablesNum = 0
        if len(tempImmovables1) != 0:
            immovablesNum = len(tempImmovables1) // 2

        '''
        for Immovable in range(len(tempImmovables1)):
            if Immovable % 2 == 1:
                tempImmovables2.append(tempImmovables1[Immovable-1] + ' ' + tempImmovables1[Immovable])
        print(tempImmovables2)
        immovablesNum = len(tempImmovables2)
        '''
        time.sleep(0.5)
        for click in range(immovablesNum):
            try:

                self.se.buttonClick('//*[@id="region_filter"]/div/div/div[3]/ul/li[' + str(click + 1) + ']')
                time.sleep(1)
                self.detailImmovable()
                time.sleep(1)
                self.se.buttonClick('//*[@id="ct"]/div[2]/div[2]/div/button')
                time.sleep(1)
                '''
                self.se.buttonClick('//*[@id="region_filter"]/div/a/span[4]')
                time.sleep(1)
                '''
                self.se.buttonClick(self.openButton)
                time.sleep(1)
                self.se.buttonClick(self.cityButton)
                time.sleep(1)
                self.se.buttonClick(self.contryButton)
                time.sleep(1)
                self.se.buttonClick(self.townButton)
                time.sleep(1)
            except:
                None

    def detailImmovable(self):
        tempImmovable1 = ['']
        try:
            # self.se.buttonClick('//*[@id="complexOverviewList"]/div/div[1]/div[3]/div/label')
            while (True):
                time.sleep(1)
                tempImmovable1[0] = self.se.driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]').text
                tempImmovable1[0] = tempImmovable1[0].replace('\n', ',')
                tempImmovable1 = tempImmovable1[0].split(',')
                s = ''
                tempImmovable2 = []
                for word in tempImmovable1:
                    if len(word) > 2 and word[:2] == '확인' or word[:3] == '등록일' or word[:4] == '거래완료':
                        tempImmovable2.append(s)
                        s = ''
                    else:
                        s += word + " "
                # immovablesNum = 0
                print(len(tempImmovable2))
                temp = self.se.scrollDown2(len(tempImmovable2))
                time.sleep(1)
                if len(tempImmovable2) == temp:
                    address = self.city + ' ' + self.contry + ' ' + self.town + ' '
                    for word in tempImmovable2:
                        self.open_output_file.write(address + word + '\n')
                    break
        except:
            None
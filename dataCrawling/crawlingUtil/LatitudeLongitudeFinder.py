from DataBase.DBConnector import DBConnector
from crawlingUtil.Selenium import Selenium
import re
import time
import winsound as ws

class LatitudeLongitudeFinder:
    db = None
    se = Selenium()
    OUTPUT_FILE_NAME = 'LatitudeLongitude.txt'
    open_output_file = None
    city = ''
    cityCode = ''
    contry = ''
    contryCode = ''
    town = ''
    townCode = ''
    inputBox = ''
    searchButton = ''

    def __init__(self, url):
        self.db = DBConnector()
        self.se.startSelenium(url)
        self.findCity()
        self.db.conn.commit()
        self.db.DBCloser()

    def findCity(self):
        city, cityCode = self.db.LLselectCity()
        self.inputBox = '//*[@id="searchboxinput"]'
        self.searchButton = '//*[@id="searchbox-searchbutton"]'
        for cityCount in range(len(city)):
            self.city = city[cityCount]
            self.cityCode = cityCode[cityCount]
            self.se.clearInputBox(self.inputBox)
            self.se.inputData(self.inputBox, '')
            self.se.inputData(self.inputBox, self.city)
            self.se.buttonClick(self.searchButton)
            time.sleep(100)
            url = self.se.get_current_url()
            temp = url.split('/')
            temp2 = (temp[6][1:]).split(',')
            Latitude = temp2[0]
            Longitude = temp2[1]
            print(self.city, Latitude, Longitude)
            self.db.LLupdateCity(self.cityCode, Latitude, Longitude)
            #self.findContry()

    def findContry(self):
        contry, contryCode = self.db.LLselectContry(self.cityCode)
        for contryCount in range(len(contry)):
            self.contry = contry[contryCount]
            self.contryCode = contryCode[contryCount]
            self.se.clearInputBox(self.inputBox)
            self.se.inputData(self.inputBox, '')
            self.se.inputData(self.inputBox, self.city + ' ' + self.contry)
            self.se.buttonClick(self.searchButton)
            time.sleep(5)
            url = self.se.get_current_url()
            temp = url.split('/')
            temp2 = (temp[6][1:]).split(',')
            Latitude = temp2[0]
            Longitude = temp2[1]
            print(self.city + ' ' +self.contry, Latitude, Longitude)
            self.db.LLupdateContry(self.cityCode, self.contryCode, Latitude, Longitude)
            self.findTown()

    def findTown(self):
        town, townCode = self.db.LLselectTown(self.contryCode)
        for townCount in range(len(town)):
            self.town = town[townCount]
            self.townCode = townCode[townCount]
            self.se.clearInputBox(self.inputBox)
            self.se.inputData(self.inputBox, '')
            self.se.inputData(self.inputBox, self.city + ' ' + self.contry + ' ' + self.town)
            self.se.buttonClick(self.searchButton)
            time.sleep(5)
            url = self.se.get_current_url()
            temp = url.split('/')
            temp2 = (temp[6][1:]).split(',')
            Latitude = temp2[0]
            Longitude = temp2[1]
            print(self.city + ' ' +self.contry + ' ' + self.town, Latitude, Longitude)
            self.db.LLupdateTown(self.contryCode, self.townCode, Latitude, Longitude)

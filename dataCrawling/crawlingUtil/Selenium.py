from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import asyncio
import time

class Selenium:

    chromePath = ''
    driver = None
    myS = None

    def __init__(self):
        self.chromePath = 'C://Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
        # 크롬드라이버 경로 ex) 'C://Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
        self.driver = webdriver.Chrome(self.chromePath)
        print("Seleniume 드라이버 적재가 완료되었습니다.\n")
        print("Selenium에 접근 준비가 완료되었습니다.\n")

    def startSelenium(self, url):
        self.driver.implicitly_wait(3)
        self.driver.get(url)

    def buttonClick(self, xPath):
        button = self.driver.find_element_by_xpath(xPath)
        button.click()
        #await asyncio.sleep(1)

    def scrollDown(self, length):
        ELEMENT = self.driver.find_elements_by_css_selector('#articleListArea > div:nth-child('+str(length)+')')[-1]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ELEMENT)
        time.sleep(0.5)
        tempImmovable1 = []
        tempImmovable2 = []
        #self.se.buttonClick('//*[@id="complexOverviewList"]/div/div[1]/div[3]/div/label')
        tempImmovable1.append(self.driver.find_element_by_xpath('//*[@id="articleListArea"]').text)
        tempImmovable1[0] = tempImmovable1[0].replace('\n', ',')
        tempImmovable1 = tempImmovable1[0].split(',')
        s = ''
        for word in tempImmovable1:
            if len(word) > 2 and word[:2] == '확인' or word[:4] == '거래완료':
                tempImmovable2.append(s)
                s = ''
            else:
                s += word + " "
        print(len(tempImmovable2))
        return len(tempImmovable2)

    def scrollDown2(self, length):
        ELEMENT = self.driver.find_elements_by_css_selector('#listContents1 > div > div > div:nth-child(1) > div:nth-child('+str(length)+')')[-1]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ELEMENT)
        time.sleep(0.5)
        tempImmovable1 = []
        tempImmovable2 = []
        #self.se.buttonClick('//*[@id="complexOverviewList"]/div/div[1]/div[3]/div/label')
        tempImmovable1.append(self.driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]').text)
        tempImmovable1[0] = tempImmovable1[0].replace('\n', ',')
        tempImmovable1 = tempImmovable1[0].split(',')
        s = ''
        for word in tempImmovable1:
            if len(word) > 2 and word[:2] == '확인' or word[:3] == '등록일' or word[:4] == '거래완료':
                tempImmovable2.append(s)
                s = ''
            else:
                s += word + " "
        print(len(tempImmovable2))
        return len(tempImmovable2)

    def inputData(self, link, temp):
        elem = self.driver.find_element_by_xpath(link)
        elem.send_keys(temp)
        elem.send_keys(Keys.RETURN)

    def clearInputBox(self, link):
        elem = self.driver.find_element_by_xpath(link)
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.DELETE)

    def get_current_url(self):
        return self.driver.current_url
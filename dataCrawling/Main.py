# -*- coding: utf-8 -*-

from datetime import datetime
from crawlingUtil.CityUtilCrawling import CityUtilCrawling
# from crawlingUtil.CityFinder import CityFinder
# from crawlingUtil.InsertCity import InsertCity
# from crawlingUtil.ImmovablesFinder import ImmovablesFinder
# from crawlingUtil.BillaJutaeckImmovablesFinder import BillaJutaeckImmovablesFinder
from crawlingUtil.LatitudeLongitudeFinder import LatitudeLongitudeFinder
import schedule
import time
import winsound

def job_day():
    for i in range(1):
        tempStr = __file__
        today = str(datetime.today().year) + "%02d" % datetime.today().month + "%02d" % datetime.today().day + '%02d' % (i+1) # str(datetime.today().year) + "%02d" % datetime.today().month + "%02d" % datetime.today().day
        rootPath = tempStr[:-16]
        #CityFinder(1)

        # 네이버 부동산 URL
        # naverImmovablesURL = 'https://new.land.naver.com/complexes?ms=37.487257,127.0568035,17&a=APT:ABYG:JGC&e=RETAIL'
        googleMap = 'https://www.google.com/maps/?hl=ko'
        # ImmovablesFinder(naverImmovablesURL)
        # InsertCity(naverImmovablesURL)
        # BillaJutaeckImmovablesFinder(naverImmovablesURL)
        LatitudeLongitudeFinder(googleMap)
        print('\n')
        print("="*120)
        print('\n\t' + str(today) + ' 크롤링 완료')
        print('\n')
        print("=" * 120)


def naviBeep():
    # 도,레,미,파,솔,라,시 Hz
    so1 = {'do':261,'re':293,'mi':329,'pa':349,'sol':391,'ra':440,'si':493}
    mel = ['si','si','si','sol','mi','mi', 'pa','re','re', 'do','re','mi','pa','sol','sol','sol']
    dur = [2,2,1,2,2,1,           2,2,1,           2,2,2,2,2,2,1]
    mel2 = ['sol','mi','mi','mi',  'pa','re','re',   'do','mi','sol','sol', 'mi','mi','mi' ]
    dur2 = [2,2,2,2,                2,2,1,             2,2,2,2,                2,2,1]
    music = zip(mel,dur)
    music2 = zip(mel2,dur2)
    for melody,duration in music:
        winsound.Beep(so1[melody],1000//duration)
    for melody,duration in music2:
        winsound.Beep(so1[melody],1000//duration)

def airplaneBeep():
    # 도,레,미,파,솔,라,시 Hz
    so1 = {'do':261,'re':293,'mi':329,'pa':349,'sol':391,'ra':440,'si':493}
    mel = ['mi','re','do',  're','mi','mi',  'mi','re','re',   're','mi','sol','sol']
    dur = [2,4,2,           2,2,2,             1,  2,   2,       1,  2,2,1]
    mel2 = ['mi','re','do',  're','mi','mi',  'mi','re','re',   'mi','re','do' ]
    dur2 = [2,4,2,                2,2,2,        1,  2,   2,         1,2,1]
    music = zip(mel,dur)
    music2 = zip(mel2,dur2)
    for melody,duration in music:
        winsound.Beep(so1[melody],1000//duration)
    for melody,duration in music2:
        winsound.Beep(so1[melody],1000//duration)


# from DataBase.DBConnector import DBConnector
# from DataBase.DataPreprocessor import DataPreprocessor

if __name__ == '__main__':

    try:
        job_day()
    except:
        naviBeep()

    airplaneBeep()

    # schedule.every().days.at("11:55").do(job_day)
    # while True:
        # schedule.run_pending()
        # time.sleep(1)
    # DB = DBConnector()
    # dp = DataPreprocessor()
    # dp.preProcessVilla()
    #print(dp.getData())

    # tempArr = DB.DBselector(dp.getData())
    # DB.InsertApart(tempArr)
    # DB.InsertOfficetel(tempArr)

    # DB.DBCloser()
    # db.InsertDB(l)
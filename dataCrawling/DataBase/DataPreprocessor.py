class DataPreprocessor:
    # FILE_NAME = '서울시 아파트 Immovables.txt'
    # FILE_NAME = '서울시 오피스텔 Immovables.txt'
    FILE_NAME = '서울시 빌라 Immovables.txt'
    data = None
    temp = []

    def __init__(self):
        with open(self.FILE_NAME, 'r', -1, "utf-8") as fileOpener:
            self.data = fileOpener.readlines()

    def preProcessAPT(self):
        for st in range(len(self.data)):

            self.data[st] = self.data[st].replace('\n', '')
            splitTemp = self.data[st].split()

            self.temp.append([[splitTemp[0]]])  # 시
            self.temp[st].append([splitTemp[1]])  # 읍/구
            self.temp[st].append([splitTemp[2]])  # 동

            stopPoint = True
            stopPoint2 = True
            pricePoint = 0
            apartPoint = 0

            for word in range(3, len(splitTemp)):
                if (splitTemp[word][0:2] == '전세' or splitTemp[word][0:2] == '월세' or splitTemp[word][0:2] == '매매'
                    or splitTemp[word][0:4] == '단기임대') and stopPoint:
                    self.temp[st].append([' '.join(splitTemp[3:word])])  # 매물 이름
                    pricePoint = word
                    stopPoint = False

                if (splitTemp[word][0:3] == '아파트' or splitTemp[word][0:3] == '재건축' or splitTemp[word][0:2] == '임대'
                    or splitTemp[word][0:4] == '오피스텔') and stopPoint2:
                    self.temp[st].append([''.join(splitTemp[pricePoint:word])])  # 가격
                    apartPoint = word
                    stopPoint2 = False

                if splitTemp[word] == '제공':
                    self.temp[st].append(splitTemp[apartPoint:word - 1])  # 매물 설명
                    ImmvoablesInfo = splitTemp[word-1:word]
                    ImmvoablesInfo.extend(splitTemp[word+1:])
                    self.temp[st].append(ImmvoablesInfo)
                    break

    def preProcessOffice(self):
        for st in range(len(self.data)):
            self.data[st] = self.data[st].replace('\n', '')
            splitTemp = self.data[st].split()

            self.temp.append([[splitTemp[0]]])  # 시
            self.temp[st].append([splitTemp[1]])  # 읍/구
            self.temp[st].append([splitTemp[2]])  # 동

            stopPoint = True
            stopPoint2 = True
            pricePoint = 0
            apartPoint = 0

            for word in range(3, len(splitTemp)):
                if (splitTemp[word][0:2] == '전세' or splitTemp[word][0:2] == '월세' or splitTemp[word][0:2] == '매매'
                    or splitTemp[word][0:4] == '단기임대') and stopPoint:
                    self.temp[st].append([' '.join(splitTemp[3:word])])  # 매물 이름
                    pricePoint = word
                    stopPoint = False

                if (splitTemp[word][0:3] == '아파트' or splitTemp[word][0:3] == '재건축' or splitTemp[word][0:2] == '임대'
                    or splitTemp[word][0:4] == '오피스텔') and stopPoint2:
                    self.temp[st].append([''.join(splitTemp[pricePoint:word])])  # 가격
                    apartPoint = word
                    stopPoint2 = False

                if splitTemp[word] == '제공':
                    self.temp[st].append(splitTemp[apartPoint:word - 1])  # 매물 설명
                    ImmvoablesInfo = splitTemp[word-1:word]
                    ImmvoablesInfo.extend(splitTemp[word+1:])
                    self.temp[st].append(ImmvoablesInfo)
                    break

    def preProcessVilla(self):
        for st in range(len(self.data)):
            self.data[st] = self.data[st].replace('\n', '')
            splitTemp = self.data[st].split()

            self.temp.append([[splitTemp[0]]])  # 시
            self.temp[st].append([splitTemp[1]])  # 읍/구
            self.temp[st].append([splitTemp[2]])  # 동

            stopPoint = True
            stopPoint2 = False
            pricePoint = 0
            apartPoint = 0

            for word in range(3, len(splitTemp)):
                if (splitTemp[word][0:2] == '전세' or splitTemp[word][0:2] == '월세' or splitTemp[word][0:2] == '매매'
                    or splitTemp[word][0:4] == '단기임대') and stopPoint:
                    # temp = ''
                    if '개의 매물사진이 있습니다.' in ' '.join(splitTemp[3:word]):
                        temp = ' '.join(splitTemp[3:word])[18:]
                    else:
                        temp = ' '.join(splitTemp[3:word])
                    self.temp[st].append([temp])  # 매물 이름
                    pricePoint = word
                    stopPoint2 = True
                    stopPoint = False

                if (splitTemp[word][0:4] == '상가주택' or splitTemp[word][0:6] == '단독/다가구' or splitTemp[word][0:2] == '빌라'
                    or splitTemp[word][0:4] == '전원주택' or splitTemp[word][0:4] == '한옥주택') and stopPoint2:

                    self.temp[st].append([''.join(splitTemp[pricePoint:word])])  # 가격
                    apartPoint = word
                    stopPoint2 = False

                if splitTemp[word] == '제공':
                    self.temp[st].append(splitTemp[apartPoint:word - 1])  # 매물 설명
                    ImmvoablesInfo = splitTemp[word-1:word]
                    ImmvoablesInfo.extend(splitTemp[word+1:])
                    self.temp[st].append(ImmvoablesInfo)
                    break

    def getData(self):
        return self.temp
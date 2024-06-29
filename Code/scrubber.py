from bs4 import BeautifulSoup
import requests



def processNewLinesOut(tempList):
    dataList = []
    for data in tempList:
        if any(c.isalpha()for c in data):
            dataList.append(data)
        elif any(c.isdigit() for c in data):
            dataList.append(data)
        
    return dataList

def scrape(zipCode):
    url = "https://forecast.weather.gov/zipcity.php"
    TEMP_DATA_LIST = []
    dataList = []
    pagetoScrape = requests.post(url, data={"inputstring" : zipCode})
    soup = BeautifulSoup(pagetoScrape.text, "html.parser")

    rawData = soup.findAll("div", attrs={"id":"current-conditions"})
    
    for data in rawData:

        dataText = data.text

        # The data in the following list will have a lot of \n characters, so it is only temporary
        TEMP_DATA_LIST = dataText.split("\n")

    # This loop will add any entries in the list that have letters or numbers to the dataList
    dataList = processNewLinesOut(TEMP_DATA_LIST)

    return dataList
    


def printListData(dataList):
    returnString = ""
    i = 1
    
    for data in dataList:
        
        returnString += data + "\n"
        if i % 2 == 0:
            returnString += "\n"
        i += 1
    
    return returnString



        



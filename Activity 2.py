import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    dateFormat = '%d/%m/%Y' 

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + random.random() * (endTime - startTime)  
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("RandomDate = ", getRandomDate("1/1/2025", "1/1/2026"))


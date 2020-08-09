from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\gyawa\Downloads\chromedriver_win32\chromedriver')
driver.get('https://www.weather-forecast.com/countries/Nepal')

places = driver.find_elements_by_xpath('//span[@class="b-list-table__item-name"]')
temp = driver.find_elements_by_xpath('//span[@class="temp"]')
number1 = len(places)
number2 = len(temp)


with open("weather1.txt","w") as f:
    for i in range(number1):
        f.write(places[i].text + " temperature  is " + temp[i].text + "\n")
driver.close()


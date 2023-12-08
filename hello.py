from bs4 import BeautifulSoup
from selenium import webdriver
import statistics
 
 
def shop1():
   driver = webdriver.Chrome()
   driver.get("https://www.net-a-porter.com/en-us/shop/clothing/jeans")
 
   soup = BeautifulSoup(driver.page_source, 'html.parser')
   response = soup.find_all("span", {"itemprop" : "price"})
   data = []
 
   for item in response:
       data.append(float(item.text.strip('$').replace(",", "")))
 
   print(data)
   return data
 
def shop2():
   driver = webdriver.Chrome()
   driver.get("https://www.madewell.com/womens/clothing/jeans")
 
   soup = BeautifulSoup(driver.page_source, 'html.parser')
   response = soup.find_all("span", "product-sales-price product-usd")
  
   data = []
 
   for item in response:
       data.append(float(item.text.strip("\n$")))
 
   print(data)
   return data
 
extracted_data1 = shop1()
extracted_data2 = shop2()
 
print(statistics.mean(extracted_data1))
print(statistics.mean(extracted_data2))
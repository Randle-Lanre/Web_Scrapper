from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
#import io

# if you get a path error while trying to run driver=webdriver.firefox(), include an excutable path as shown below





driver= webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get("https://www.konga.com/games-consoles-5211")
SCROLL_PAUSE_TIME = 1.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
html=driver.page_source
soup=BeautifulSoup(html, "html.parser")

console_containers= soup.find_all('li', class_='product-block-container')

filename= "konga_price_list.csv"

f=open(filename, "w", encoding="utf-8") 

headers="Product_name, Price, Store_owner\n"


f.write(headers)



for containers in console_containers:
	

	game_containers=containers.find_all('div', class_='product-block')
	game=game_containers[0].div.a
	prod=game.text
	

	price_containers=containers.find_all('div', class_='original-price original-price-bold')
	
	try: 
		current=price_containers[0].text
	except IndexError:
		print('there is a special price for this item')


	stores_containers= containers.find_all('a', class_='truncate')
	strs=stores_containers[0].text

	print('Brand: '+ prod)

	print('Original Price is: '+ current)
	print('Store ' + strs)



	f.write(prod+","+current.replace(",", ".")+", "+ strs+ "\n")

f.close()






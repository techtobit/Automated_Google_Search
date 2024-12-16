from selenium import webdriver
from helium import *
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from MySql import MySQL_DB

import time
import re



class Search:
	def __init__(self, keyword):
		# user_agent = UserAgent()
		# user_string = user_agent.random
		# options = webdriver.ChromeOptions()
		# options.add_argument(f'user-agent={user_string}')
		# options.add_argument("--headless")
		# options.add_argument("--disable-gpu")
		# options.add_argument("--no-sandbox")

		# self.browser=webdriver.Chrome(options=options)
		# set_driver(self.browser)

		# Use Helium 
		self.keyword=keyword
		self.browser = start_chrome(headless=True)
		

	def gSarch(self):
		go_to("https://www.google.com")
		search_box = find_all(S("textarea[name='q']"))[0]
		write(self.keyword, into=search_box)
		press(ENTER)
		time.sleep(5)

	def getResult(self):
		try:
			wait_until(lambda: len(find_all(S("cite"))) > 0, timeout_secs=10)
			elements = find_all(S("cite"))
			urls = []
			if len(urls) > 1:
				urls.clear()

			for element in elements:
				text=element.web_element.text.strip()
				match = re.match(r'https?://\S+', text)
				if match:
						urls.append(match.group(0)) 
			print(urls)
			return urls
		except Exception as e:
			print(f'Failed to find elements or result. {e}')
	
	def saveResult(self, urls):
		MySQL_DB.insertDataInDB(urls, self.keyword)

	def closeBrowser(self):
		kill_browser()




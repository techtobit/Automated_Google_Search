from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time

options=Options()
options.headless=True

class Search:
	def __init__(self):
		self.browser = webdriver.Chrome(options=options)

	def gSarch(self,keyword):
		print('key-', keyword)
		self.browser.get('http://www.google.com')
		search = self.browser.find_element(By.NAME, 'q')
		search.send_keys(keyword)
		search.send_keys(Keys.RETURN)
		time.sleep(15)
		self.browser.quit()


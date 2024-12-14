from selenium import webdriver
from helium import *
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
		# self.browser =  webdriver.Chrome(options=options)

		# Use Helium 
		self.browser =  start_chrome(headless=True)

	def gSarch(self,keyword):
		# self.browser.get('http://www.google.com')
		# search = self.browser.find_element(By.NAME, 'q')
		# search.send_keys(keyword)
		# search.send_keys(Keys.RETURN)
		# time.sleep(3)

		# Use Helium 
		go_to("https://www.google.com")
		search_box = find_all(S("textarea[name='q']"))[0]
		write('python', into=search_box)
		press(ENTER)
		time.sleep(3)

	def getResult(self):
		# results=WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//cite")))
		# urls= [result.text for result in results if result.text.strip()]
		
		# Use Helium 
		# wait_until(lambda: len(find_all(S("cite"))) >0, timeout_secs=10)
		# elements=find_all(S("cite"))
		# urls=[element.web_element.text for element in elements if element.web_element.text.strip()]


		wait_until(lambda: len(find_all(S("cite"))) > 0, timeout_secs=10)
		elements = find_all(S("cite"))
		urls = [element.web_element.text for element in elements if element.web_element.text.strip()]
		print(urls)

	def closeBrowser(self):
		# self.browser.close()
		kill_browser()



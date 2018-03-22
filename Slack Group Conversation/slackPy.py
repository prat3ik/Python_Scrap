from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://testingggworkspace.slack.com/messages/C9RUR7N3C/")

driver.find_element_by_xpath("//*[@name='email'][@type='email']").send_keys('patrsmith1@gmail.com')
driver.find_element_by_xpath("//*[@name='password'][@type='password']").send_keys('abc@123.com')
driver.find_element_by_id("signin_btn").click()

messageEle = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'msg_input')))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify()) ,{"class":"c-message__body"}

senders = soup.findAll("a", {"class": "c-message__sender_link"})
messages = soup.findAll("span", {"class": "c-message__body"})


for sender_name,message_content in zip(senders,messages):
	print(sender_name.text+ " 	:	"+message_content.text)
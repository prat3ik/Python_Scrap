from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.google.com/flights")
text_fields = driver.find_elements(By.CSS_SELECTOR, "div.gws-flights-form__location-text")

text_fields[0].click()
sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Where from?']").send_keys("Los Angeles")
sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Where from?']").send_keys(Keys.RETURN)

sleep(2)

text_fields[1].click()
sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Where to?']").send_keys("New York")
sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Where to?']").send_keys(Keys.RETURN)

sleep(2)

date_text_fields = driver.find_elements(By.CSS_SELECTOR, "span.gws-flights-form__date-content")
date_text_fields[0].click()
sleep(5)

flight_dates = driver.find_elements(By.XPATH, "//span[contains(@class,'gws-travel-calendar__annotation')]/../preceding-sibling::div[@class='gws-travel-calendar__day-label']")
flight_costs = driver.find_elements(By.CSS_SELECTOR, "span.gws-travel-calendar__annotation")

for date,cost in zip(flight_dates,flight_costs):
	print ("Date: " + date.text + "   -->   Cost: " + cost.text)

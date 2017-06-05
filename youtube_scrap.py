from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=" + "coldplay")

results = driver.find_elements_by_xpath('//div[@class="yt-lockup-content"]')

print(len(results))

for result in results:
	video_link = result.find_element_by_css_selector(".yt-uix-tile-link")
	video_title = video_link.get_attribute("title")
	video_url = video_link.get_attribute("href")
	print("Title : {0} \nUrl   : {1} \n".format(video_title, video_url))

driver.quit()
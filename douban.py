from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://www.douban.com")

driver.find_element_by_name("form_email").send_keys("1______5")
driver.find_element_by_name("form_password").send_keys("c______c")
driver.find_element_by_id("captcha_field").send_keys("bottle")
driver.find_element_by_xpath('//input[@class="bn-submit"]').click()

time.sleep(3)

driver.save_screenshot("douban.png")

# with open("douban.html", "w") as file:
# 	file.write(driver.page_source)

driver.quit()


# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")

time.sleep(3)
time

js = "document.body.scrollTop=10000"

driver.save_screenshot("douban.png")

driver.execute_script(js)
time.sleep(10)

driver.save_screenshot("newdouban.png")

driver.quit()
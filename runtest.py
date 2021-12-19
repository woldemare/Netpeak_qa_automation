from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from testpage import *

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://netpeak.ua")
start_test = Netpeak(driver)
start_test.about_team()
start_test.personal_account()
start_test.check_color()
driver.quit()
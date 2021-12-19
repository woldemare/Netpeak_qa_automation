from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random

class Netpeak:
    def __init__(self, driver):
        self.driver = driver
        self.about_us = "//li[@data-content='58']"
        self.team_button = "//div[@class='links-box']//a[@href='/team/']"
        self.part_of_team = "//a[@class='tn-atom']"
        self.login = '//*[@id="login"]'
        self.password = '//*[@id="password"]'
        self.personal_account_button = '//div[@class="justify-right options"]//a[@class="custom-link"]'
        self.checkbox = '//md-checkbox[@aria-label="gdpr"]'
        self.enter_button = '//button[@class="enter md-button md-ink-ripple"]'
        self.error_with_red_color = '//md-input-container//input[@aria-invalid="true"]'

    def about_team(self):
        netpeak_window = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, self.about_us).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.team_button))).click()
        self.driver.find_element(By.XPATH, self.part_of_team).click()
        work_page_title = self.driver.title
        assert work_page_title == "Команда Netpeak Украина. Присоединяйтесь!", \
            "Netpeak job page was not open"
        if work_page_title == "Команда Netpeak Украина. Присоединяйтесь!":
            print('Opened page about working in Netpeak')
        else:
            print('Wrong page is open')
        script = "dataLayer.push({'event':'gtm-ua-event', 'gtm-event-category':'Карьера', " \
                 "'gtm-event-action':'Нажатие на кнопку «Я хочу работать в Netpeak»', " \
                 "'gtm-event-label':document.location.href})"
        self.driver.execute_script(script)  # пытался проверить кнопку "Я хочу работать в Netpeak...."
        self.driver.switch_to.window(netpeak_window)
        assert self.driver.title == "Команда Netpeak Украина. Присоединяйтесь!", \
            "Netpeak job page was not open"

    def personal_account(self):
        self.driver.find_element(By.XPATH, self.personal_account_button).click()
        wait1 = WebDriverWait(self.driver, 10)
        wait1.until(EC.element_to_be_clickable((By.XPATH, self.personal_account_button))).click()
        random_letters = string.ascii_lowercase
        window_personal_account = self.driver.window_handles[2]
        self.driver.switch_to.window(window_personal_account)
        assert self.driver.title == "Вход в «Личный кабинет»", \
            "Wrong page was open"
        self.driver.find_element(By.XPATH, self.login).send_keys(random_letters)
        self.driver.find_element(By.XPATH, self.password).send_keys(random_letters)
        element = self.driver.find_element(By.XPATH, self.enter_button)
        login_button = element.is_enabled()
        if login_button == False:
            print('Login button disabled')
        else:
            print('Login button enabled')
        self.driver.find_element(By.XPATH, self.checkbox).click()
        self.driver.find_element(By.XPATH, self.enter_button).click()

    def check_color(self):
        element = self.driver.find_element(By.XPATH, self.error_with_red_color)
        self.error_with_red_color = element.is_enabled()
        if self.error_with_red_color == True:
            print('Login and password fields is red (check by XPath)')
        else:
            print('Error notification is not red')
        login_color = self.driver.find_element(By.XPATH, self.login).value_of_css_property('border-color')
        assert login_color == 'rgb(221, 44, 0)', "Login field is not red"
        password_color = self.driver.find_element(By.XPATH, self.password).value_of_css_property('border-color')
        assert password_color == 'rgb(221, 44, 0)', "Password field is not red"
        if login_color and password_color == 'rgb(221, 44, 0)':
            print('Login and password fields is red (check by RGB)')
        else:
            print('Login and password fields is not red')
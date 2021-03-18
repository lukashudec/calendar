import time

from selenium import webdriver


def before_scenario(context, scenario):
    if 'web_test' in context.tags:
        context.driver = webdriver.Chrome('C:/Users/lenovo/Downloads/chromedriver_win32_87/chromedriver.exe')
        context.driver.implicitly_wait(2)


def after_scenario(context, scenario):
    if 'web_test' in context.tags:
        time.sleep(1)
        context.driver.close()

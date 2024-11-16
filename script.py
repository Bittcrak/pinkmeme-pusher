import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
# from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



class pinkmeth:
    def proxy_req(address):
        options = Options()
        options.add_argument(f'--proxy-server={address}')
        options.headless=True
        driver = webdriver.Firefox(options=options)
        return driver
    def scroll(driver, url):
        driver.get(url)
        i=0
        height=driver.execute_script("return document.body.scrollHeight;")
        while (i<height):
            driver.execute_script(f"window.scrollTo(0, {i*100});")
            i+=10
    def leave(driver):
        driver.quit()
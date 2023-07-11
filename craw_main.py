from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from requests.adapters import HTTPAdapter
from fake_useragent import UserAgent
from selenium import webdriver
import requests
import time

class CrawlMain:
    def __init__(self, headers=None) -> None:
        if headers:
            self.headers = headers
        else:
            self.ua = UserAgent().random
            self.headers = {
                'user-agent': self.ua
            }

    # 使用request直接获取
    def response_text(self, url, timeout=5):
        response = ''
        try:
            s = requests.session()
            # max_retries=3 重试3次
            s.mount('http://', HTTPAdapter(max_retries=3))
            s.mount('https://', HTTPAdapter(max_retries=3))
            response = s.request("GET", url=url, timeout=timeout, headers=self.headers)
        except Exception as e:
            raise e
        finally:
            return response

    # 使用selenium获取内容
    def selenium_text(self, url, timeSleep=0):
        text = ''
        browser = None
        try:
            # 启动Chrome浏览器
            driver_manager = ChromeDriverManager()
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            option.add_argument('blink-settings=imagesEnabled=false')

            desired_capabilities = DesiredCapabilities.CHROME

            desired_capabilities["pageLoadStrategy"] = "none"
            # 指定Chrome驱动的路径
            service = Service(driver_manager.install())
            # 创建Chrome浏览器对象
            browser = webdriver.Chrome(options=option, service=service)
            browser.set_page_load_timeout(15)  # 页面加载超时时间
            browser.set_script_timeout(15)  # 页面js加载超时时间
            # browser = webdriver.Chrome(service=service)
            browser.get(url)
            time.sleep(timeSleep)
            text = browser.page_source
        except Exception as e:
            raise e
        finally:
            if browser:
                browser.quit()
            return text

from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
import os

# Create your views here.

def index(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_path = "/home/intel/Downloads/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.skrill.com/en/crypto/live-cryptocurrency-prices/")
    #html = driver.page_source
    table = driver.find_elements_by_xpath('//table[@class="skrill-live-crypto"]/tbody/tr')

    live_data = []
    for data in table:
        coins = data.find_element_by_xpath('./td[1]/a/b[2]').text
        price = data.find_element_by_xpath('./td[3]').text
        market_cap = data.find_element_by_xpath('./td[6]').text
        live_data.append({'coins':coins,'price':price, 'market_cap':market_cap})

    driver.close()
    return render(request, 'data/home.html', {'live_data': live_data})

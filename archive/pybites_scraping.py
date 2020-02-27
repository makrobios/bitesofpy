import re
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

DOWNLOAD_DIR = '/home/ch/pybites/archive/'
# settings that prevent popup dialog when downloading zip files
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList',2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', DOWNLOAD_DIR )
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

browser = webdriver.Firefox(firefox_profile=fp)
browser.implicitly_wait(5)
url='https://codechalleng.es/login/'
browser.get(url)
user = browser.find_element_by_css_selector('#id_username')
user.send_keys('makrobios')
password = browser.find_element_by_css_selector('#id_password')
password.send_keys('3QQsC4nqEgcMTDj))')
browser.find_element_by_css_selector('.mui-btn--primary').click()
browser.get('https://codechalleng.es/bites/catalogue')

get_last_bite_number = browser.find_element_by_css_selector("table tr:last-child td")
last_bite_number = int(re.findall(r"\d+", get_last_bite_number.text)[0])

for bite in range(1, last_bite_number + 1):
    if not os.path.exists(f'/home/ch/pybites/archive/pybites_bite{bite}.zip'):
        try:
            browser.get(f'https://codechalleng.es/bites/{bite}')
            githubBtn = browser.find_element_by_id('githubDropdown')
            githubBtn.click()
        except NoSuchElementException:
            continue
    
        downloadBtn = browser.find_element_by_id('downloadBiteBtn')
        downloadBtn.click()
        time.sleep(1)

#browser.get('https://codechalleng.es/bites/api/downloads/bites/1/')


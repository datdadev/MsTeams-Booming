import random

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import threading

#List of username
name = ['Tony', 'Jora', 'Max']


def browser(name):
    opt = ChromiumOptions()
    #opt.add_argument("--headless")
    #opt.add_argument("start-maximized")
    #opt.add_argument("disable-infobars")
    opt.add_argument("use-fake-ui-for-media-stream")
    opt.add_experimental_option("excludeSwitches", ["enable-logging"])
    opt.add_experimental_option("detach", True)
    opt.add_argument("--disable-extensions")
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-application-cache')
    opt.add_argument('--disable-gpu')
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_argument("test-type")
    opt.add_argument("--js-flags=--expose-gc")
    opt.add_argument("--enable-precise-memory-info")
    opt.add_argument("--disable-default-apps")
    #----------
    opt.add_argument("--disable-background-networking")
    opt.add_argument("--disable-client-side-phishing-detection")
    opt.add_argument("--disable-default-apps")
    opt.add_argument("--disable-hang-monitor")
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--disable-prompt-on-repost")
    opt.add_argument("--disable-sync")
    opt.add_argument("--disable-web-resources")
    opt.add_argument("--enable-automation")
    opt.add_argument("--enable-logging")
    opt.add_argument("--force-fieldtrials=SiteIsolationExtensions/Control")
    opt.add_argument("--ignore-certificate-errors")
    opt.add_argument("--log-level=0")
    opt.add_argument("--metrics-recording-only")
    opt.add_argument("--no-first-run")
    opt.add_argument("--password-store=basic")
    opt.add_argument("--test-type=webdriver")
    opt.add_argument("--use-mock-keychain")

    # Message Information
    msgID = '1234567890123'
    url = 'https://teams.microsoft.com/_#/l/meetup-join/19:...@thread.tacv2/'+msgID+'?context=%7B%22Tid%22%3A%22...'
    print(url)

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=opt)
    driver.get(url=url)

    try:
        myElem = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "username")))
        print("Page is ready!")
        driver.find_element("id", "username").send_keys(name)

        driver.find_element(By.XPATH,
            "//button[@class='join-btn ts-btn inset-border ts-btn-primary'][.='Join now']"
        ).click()
    except TimeoutException:
        print("Loading took too much time!")

# Number of browsers to spawn
N = 1

thread_list = list()

# Start Booming
for i in range(0, N):
    randNum = random.randint(0, len(name))
    t = threading.Thread(name='Browser: {}'.format(i), target=browser(name=name[randNum]))
    name.pop(randNum)
    t.start()
    print(t.name + ' started!')

    t.join()
    thread_list.append(t)

print('Completed!')
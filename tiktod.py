from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(1024, 650)

def ifExist(xpath):
        try:
            driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

def loop():
    url = driver.current_url
    if url == "https://bugsliker.me/index.php?info=Session_Expired":
        login()
    else:
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/fieldset/div/div/a[2]").click()
        time.sleep(1)
        driver.get("https://fireliker.com/autoViews.php")
        time.sleep(3)
        select = Select(driver.find_element_by_xpath("//*[@id=\"select\"]"))
        select.select_by_visible_text("1000 VIEWS")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[1]/div/div[2]/div/form/button").click()
        time.sleep(300)
        loop()

def login():
    driver.get("https://fireliker.com/welcome.php")
    time.sleep(22) //Anticipate to cloudflare check
    if ifExist("/html/body/div[2]/div[2]/div/form/fieldset/div[1]/div/input"]"):
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/form/fieldset/div[1]/div/input").send_keys(username)
        time.sleep(1)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(1)
        driver.get("https://fireliker.com/welcome.php")
        time.sleep(1)
        loop()
    else:
        loop()

system("cls")
username = "YOUR_USERNAME" #Change YOUR_USERNAME to your Tik Tok username
system("cls")
tiktod = pyfiglet.figlet_format("TIKTOD", font="slant")
print(tiktod)
print("Author: https://github.com/kangoka")
login()

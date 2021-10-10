from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#import start
import os
from selenium.webdriver.common.keys import Keys
import win32com.client
from time import sleep
import login
import schedual
from posted import posted
from description import addDescription


path = "C:/Users/rudra/Desktop/instagram/post/"
files = os.listdir(path)
# opening connection
Option = Options()
Option.add_argument("--disable-infobars")
Option.add_argument("start-maximized")
Option.add_argument("--disable-extensions")
Option.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_options=Option, executable_path=  "C:\chromedriver.exe")

driver.get("https://business.facebook.com/creatorstudio/")

# adding wait
wait = WebDriverWait(driver, 1200)

# switching to Instagram Login page
element = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="media_manager_chrome_bar_instagram_icon"]')
    )
)

element.click()

# clicking on login button
insta_Login = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Instagram Login']"))
)
insta_Login.click()

# making a login
print("Making a Login")
# login.greeting()


def whole(c):

    # First left control i.e clicks(Create Post -> Insta Feed)
    Create_Post_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[text()='Create Post']",
            )
        )
    )
    Create_Post_btn.click()
    Insta_Feed = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Instagram फीड']"))
    )
    Insta_Feed.click()
    sleep(3)

    # adding post//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input
    
    add_content = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="creator_studio_sliding_tray_root"]/div/div/div[2]/div[1]/div/div[5]/div',
            )
        )
    )
    add_content.click()
    print(files[c], "is been going to schedual")
    driver.find_element_by_xpath("//input[@type='file']").send_keys(
        "C:/Users/RUDRA/Desktop/instagram/post/" + files[c]
    )
    
    addDescription(driver, wait)
    # clicking Schedual Button
    aaa = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@class,'_8122')]"))
    )

    aaa.click()
    WebDriverWait(driver, 400).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Schedule']"))
    )
    if c ==  00:
        driver.find_element_by_xpath("//*[text()='Publish']").click()
        sleep(10)
    else:
        # Adding time and date
        schedual.schedualtime(driver)
        schedual.schedualdate(driver)
        # choosing sleep time
        if files[c].endswith(".mp4"):
            sleep(7)
        else:
            sleep(1)

        # click on schedual button
        schedual_btn = driver.find_element_by_xpath(
            '//*[@id="creator_studio_sliding_tray_root"]/div/div/div[3]/div[2]/button'
        )

        schedual_btn.click()

    sleep(14)
    posted(files[c])
    print("============================================")


for c in  range(len(files)):
    print(c)
    whole(c)

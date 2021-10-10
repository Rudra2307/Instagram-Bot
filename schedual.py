import datetime
from selenium.webdriver.common.keys import Keys
from time import sleep


x = datetime.datetime.now()
x = x + datetime.timedelta(hours=2, minutes=0)
date_str = x
print(x)


def minutes():
    global x
    global date_str
    hrs_int = int(x.strftime("%H"))
    if hrs_int == 00 or hrs_int < 8:
        x = x + datetime.timedelta(hours=9)
    if hrs_int < 20:
        x = x + datetime.timedelta(hours=1)
    else:
        x = x + datetime.timedelta(minutes=15)
    hrs_int = int(x.strftime("%H"))
    date_str = x.strftime("%d-%m-%Y")
    mins_int = int(x.strftime("%M"))
    print(hrs_int, date_str, mins_int)
    return mins_int, hrs_int


def schedualdate(d):
    date = d.find_element_by_xpath("//input[@placeholder='दिनांक-महिना-वर्ष']")
    date.click()
    date.send_keys(Keys.CONTROL, "a")
    date.send_keys(date_str)
    print("on", date_str)


def schedualtime(d):
    mins, hrs = minutes()
    mins_str = str("{:0>2d}".format(mins))
    hrs_str = str("{:0>2d}".format(hrs))
    d.find_element_by_xpath("//*[text()='Schedule']").click()
    hours = d.find_element_by_xpath("//*[starts-with(@class,'_4nx5')]")
    hours.click()
    hours.send_keys("0")
    hours.send_keys(hrs_str)
    hours.send_keys(Keys.TAB, "0", "0", mins_str)
    print(hrs_str, "hrs &", mins_str, "mins")

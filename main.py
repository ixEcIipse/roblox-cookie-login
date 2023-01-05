import os
try:
 from selenium import webdriver
 from adm4.main import *
except:
    input("press enter to install required moudules, or ctrl + c to quit: ")
    os.system("pip install adm4 && pip install selenium")                    ### installs required modules
    os.system("cls")
    print("finished installing, please restart the terminal")


close()
browsr = input("""
[1] Chrome
[2] Firefox
[3] Edge

[+] choose a number> """)  ### selects browser
if browsr == '1':
    print("Chrome selected")
    if is_Admin():
     driver = webdriver.Chrome()
    else:
     print("administrator privlages needed to edit chromium browser cookies, please restart terminal as administrator.") ### chromium browsers require admin privlages to edit cookies, honestly just use firefox
     exit()
elif browsr == '2':
    print("Firefox selected")
    driver = webdriver.Firefox()
elif browsr == '3':
    print("Edge selected")
    if is_Admin():
     driver = webdriver.Edge()
    else:
     print("administrator privlages needed to edit chromium browser cookies, please restart terminal as administrator.") ### chromium browsers require admin privlages to edit cookies
     exit()
else:
    print("not a number")
    exit()
COKE = input("cookie: ")
driver.get("https://www.roblox.com/home")
driver.add_cookie({"name" : ".ROBLOSECURITY", "value" : f"{COKE}"}) ### adds the cookie
print(driver.get_cookies())




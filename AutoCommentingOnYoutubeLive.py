################## Auto commenting on yt-live-video #################################

# ------------------- Before Executing Code ------------------------
# 1. opne CMD
# 2. Navigate (cd) to the directory where Chrome is installed. The default location is usually C:\Program Files\Google\Chrome\Application. but i did --> cd "C:\Program Files (x86)\Google\Chrome\Application"
#  ----- mat krna chrome.exe --remote-debugging-port=9222/ or what ever you want port which is free
#  ----- muje nhi pata bc bas login window pe liye keya ye tamjam
# 3. make one folder --> i create in desktop name ChromeSessionData
# 4. chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\DICE\OneDrive\Desktop\ChromeSessionData" 

# ye bas essi liye taki jispe login kr rakha he wo wala chrome khule
# warna new instance/window/browser/(bas samaj jao) lunch hota he hr barr





# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys


# print("plzz.... yr mat masti karoo bhagwan jiiii..... esse kara do")
# browser = webdriver.Chrome() # I use Chrome() coz i use chrome XD
# browser.get('https://youtube.com') # complete address of site in string and get() will do the rest , apna dimag mat lagao ree
# time.sleep(5) # aree baba code 5 sec rokega taki site complete load hojaye then next line of code work kare warna erroor aaa skta he bacha
# search_box = browser.find_element('css selector','ytd-searchbox') # ytd-searchbox is class name for search input tag on YT
# search_box.send_keys("ye bataa") # what ever string you pass goes in search box
# search_box.send_keys(Keys.ENTER) # ab ye to khud samaja bsdk





from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


print("plzz.... yr mat masti karoo bhagwan jiiii..... esse kara do")

opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")
browser = webdriver.Chrome(options = opt)  
browser.get('https://youtube.com')  


# time.sleep(5)  
# search_box = browser.find_element('css selector','ytd-searchbox')  
# search_box.send_keys("ye bataa")  
# search_box.send_keys(Keys.ENTER)  








#code was deleted






# just to hold browser window
input("Enter to close the browser...") 
# jugad kahte 
# agar VS Code pe ho to sida terminal kill kr doo

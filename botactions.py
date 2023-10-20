import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
import undetected_chromedriver as uc
from seleniumbase import BaseCase
import time
import random


class Tiktokbot(BaseCase):
    
    timers = [
        "0", "2", "1", "3", "4", "5", "6", "7", "8", "9"
]
    list = [True, False]
    
    loginVariables = [
    "https://www.tiktok.com/login/phone-or-email/email",
    "//input[@placeholder='Email or username']",
    "//input[@placeholder='Password']", "//button[@type='submit']"
]

    scrollVariables = [
        '//*[@id="one-column-item-2"]', 
        '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]', 
        '//*[@id="app"]/div[2]/div[4]/div/div[1]/div[3]/div[2]/div[2]'
    ]
    
    scrollVariables1 = {
        "canvas": '//*[@id="one-column-item-0"]/div'
    }
    
    scrollVariablesInteraction = {
        "like_button" : '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button[1]' ,
        "save_button": '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button[3]/span',
        "comment_field": '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div/span/span',
    }
    
    followInteractionVariables ={
        "follow_link" : '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/a[2]',
        "follow_btn" : '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/button'
    }
    
    uploadVariables ={
        "upload_link" : 'https://www.tiktok.com/creator-center/upload?from=upload',
        "select_file_btn" : '//*[@id="root"]/div/div/div/div/div/div/div/div/div[5]/button'
    }
    
    commentfile = "comments.txt"
    
    def __init__(self, email, password, profile, directory):
        self.email = email
        self.password = password
        self.islogedIn = True
        self.options = webdriver.ChromeOptions()
        self.profile = profile
    
        self.directory =directory
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--user-data-dir='+self.directory)
        self.options.add_argument('--profile-directory='+self.profile)
        #self.options.add_argument('--proxy-bypass-list=<-loopback>')
        self.driver = uc.Chrome(options=self.options, use_subprocess=True)
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
        )
        self.actions = ActionChains(self.driver)
       
    
    def shoutout():
        print("shout out to Zinkq on github")
        
    def getBot(self):
        return self.driver

        
    def autoscroll(self,times,mute):
    
        self.islogedIn = True
        if self.islogedIn :
            self.driver.get("https://www.tiktok.com/foryou")
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="one-column-item-2"]' )))            
            canvas = self.driver.find_element("xpath", Tiktokbot.scrollVariables1['canvas'])     
            canvas.click()
            print("canvas clicked")
     
            
           
            time.sleep(5)
            for x in range(times):
                
            #waits for the browser to load
                self.driver.implicitly_wait(2)
                WebDriverWait(self.driver,10)
                downbutton = ""
                Vidlength = ""
                while downbutton == "" and Vidlength == "":
                    try:
                        print("finding bttons")
                        downbutton = self.driver.find_element("xpath", Tiktokbot.scrollVariables[1])
                        Vidlength = self.driver.find_element("xpath", Tiktokbot.scrollVariables[2]).get_attribute("innerText")
                        sleep_duration = str(Vidlength[Vidlength.find("/")+1: len(Vidlength)])
                        get_time = (int(sleep_duration[0:2])*60) + int(sleep_duration[3:len(sleep_duration)])
                        print("finding bttons done")
                    except:
                        time.sleep(30)
                        print("\n unable to find some elements \n trying again \n \n")
                
                
               
                
                    time.sleep(get_time)
                    print("about", get_time, "seconds till scroll")
              
                    try:
                        print("scrolling")
                        downbutton.click()
                        
                            
                    except:
                        print("unable to click button as element is not interactable \n trying again in a few seconds")
                    print("scrolled for the "+ str(x) + "time")
        else:
            print("ur not logged in")
            
            
        
        
    
    def wait(self,sleep):
        time.sleep(sleep)
        
    def quit_bot(self):
        print("working here")
        self.driver.quit()
        print("bot quitted")
        
    #currently not working
 




